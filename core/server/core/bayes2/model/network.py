from .inetwork import *


def family_edges(edges: dict, key):
    if key not in edges:
        return set()
    return set(edges[key] + [b for a in edges[key] for b in family_edges(edges, a)])


class DynamicBayesianNetwork(INetwork):
    node_temporal: list

    edges: dict
    observer_data: list
    all_node_handle_temporal: list

    def __init__(
            self,
            deployment_scenario=None,
            attack_graph=None,
            exploitability: str = 'High',
            remediation_level: str = 'Unavailable',
            report_confidence: str = 'Confirmed',
            time_step: int = INetwork.DEFAULT_TIME_STEP,
            time_layer: int = INetwork.DEFAULT_TIME_LAYER,
            node_temporal=None,
            countermeasures=True,
            observer_data=None
    ) -> None:
        super().__init__()
        if deployment_scenario is None:
            deployment_scenario = {}
        if node_temporal is None:
            self.node_temporal = []
        else:
            self.node_temporal = node_temporal
        if attack_graph is None:
            attack_graph = {}
        if observer_data is None:
            observer_data = []

        self.network = pysmile.Network()
        self.edges = {}
        self.all_node_handle_temporal = []

        self.nodes = {}
        if countermeasures:
            self.countermeasures = deployment_scenario['countermeasures']
        else:
            self.countermeasures = []
        self._parser_assets(deployment_scenario['assets'])
        self.security_goals = deployment_scenario['security_goals']
        self._parser_vulnerabilities(deployment_scenario['cves'])
        self.attack_graph = attack_graph
        self.time_step = time_step
        self.time_layer = time_layer
        self.target = deployment_scenario['target']
        self.observer_data = observer_data

        Node.reset_id()

        # init value
        list_node_vul = {}

        # Init coverage : dict {'Name CVE': [coverage1, coverage2]}
        init_coverage = self._init_coverage()

        # Temporal
        self.exploitability = E_CVSS.get(exploitability, 1.00)
        self.remediation_level = RL_CVSS.get(remediation_level, 1.00)
        self.report_confidence = RC_CVSS.get(report_confidence, 1.00)

        # Attack_graph to BDN
        for tmp in self.attack_graph['nodes']:
            if tmp['is_attacker'] == TYPE_ATTACKER:
                node = NodeCPT(name="Attacker_{}_{}".format(
                    tmp['label'], tmp['id']))
                node.set_attacker()
                list_node_vul[tmp['id']] = node
                self.add_node(node)
            elif tmp['is_attacker'] == TYPE_CVE:
                vul = [x for x in self.vulnerabilities[tmp['asset_id']]
                       if x['cve_id'] == tmp['cve_id']][0]
                if 'relation' in tmp:
                    node = NodeCPT(
                        name="Vulnerability_{}_{}".format(
                            tmp['name'], tmp['id']),
                        probability=vul['exploitabilityScore'] * self.exploitability * self.report_confidence * self.remediation_level,
                        impact=vul['impactScore'],
                        asset_id=tmp['asset_id'],
                        cve_id=tmp['cve_id'],
                    )
                else:
                    node = NodeCPT(
                        name="Vulnerability_{}_{}".format(
                            tmp['cve_id'], tmp['id']),
                        probability=vul['exploitabilityScore'] * self.exploitability * self.report_confidence * self.remediation_level,
                        impact=vul['impactScore'],
                        asset_id=tmp['asset_id'],
                        cve_id=tmp['cve_id'],
                    )
                list_node_vul[tmp['id']] = node
                self.add_node(node)
                self.assets[tmp['asset_id']]['cve_nodes'].append(node)
        relations = []
        for link in self.attack_graph['edges']:
            source = list_node_vul[link['source']]
            target = list_node_vul[link['target']]
            relations.append([source.handle, target.handle])

        for p, c in relations:
            self.edges.setdefault(p, []).append(c)

        # Set DBN
        self._auto_set_temporal_network()

        # Set Arc
        for link in self.attack_graph['edges']:
            self.add_link(list_node_vul[link['source']], list_node_vul[link['target']])

        # auto set definition
        self._auto_set_node_definition(init_coverage)

        # auto set definition temporal
        self._auto_node_temporal_definition()

        # auto set evidence
        self._auto_set_evidence()

    def _auto_set_temporal_network(self):
        all_temporal_network = []
        for node_handle in self.nodes:
            node = self.nodes[node_handle]
            for temporal in self.node_temporal:
                if node.asset_id == temporal['asset_id'] and node.cve_id in temporal['cves']:
                    self.all_node_handle_temporal.append(node_handle)
                    all_temporal_network += [node_handle] + list(family_edges(self.edges, node.handle))

        all_node_temporal = list(set(all_temporal_network))
        for node_handle in all_node_temporal:
            self.set_node_temporal_type(node_handle)
            if node_handle in self.all_node_handle_temporal:
                self.network.add_temporal_arc(node_handle, node_handle, 1)
        self.network.set_slice_count(self.time_step)
        self._update_network()

    def _auto_node_temporal_definition(self):
        for node_handle in self.nodes:
            if self.network.get_node_temporal_type(
                    node_handle) == pysmile.NodeTemporalType.PLATE and node_handle in self.all_node_handle_temporal:
                probability = round(
                    self.nodes[node_handle].new_probability, INetwork.DECIMAL)
                number_parents = len(self.network.get_parents(node_handle))
                arr = [None] * (number_parents + 1)
                l = []
                generate_all_binary(number_parents + 1, arr, 0, l)
                l.reverse()
                cpts = []
                for val in l:
                    n = len(val)
                    if val[n - 1] == 1:
                        if val == [0] * (n - 1) + [1]:
                            cpt = 0.0
                        else:
                            cpt = 1.0
                    else:
                        number_true = sum(val[:n - 1])
                        cpt = 1 - pow(1 - probability, number_true)
                    cpts += [round(cpt, INetwork.DECIMAL), round(1 - cpt, INetwork.DECIMAL)]
                self.network.set_node_temporal_definition(node_handle, 1, cpts)

        self._update_network()

    def _auto_set_evidence(self):
        for observer in self.observer_data:
            for node_handle in self.nodes:
                node = self.nodes[node_handle]
                if node.cve_id == observer['cve_id'] and node.asset_id == observer['asset_id']:
                    for ob in observer['observer_data']:
                        evidence = 1
                        if not ob['value']:
                            evidence = 0
                        try:
                            self.network.set_temporal_evidence(node.handle, ob['step'], evidence)
                            print('Set node', node.cve_id, ob['step'], evidence)
                        except Exception as e:
                            print('Error message', str(e))

        self._update_network()
