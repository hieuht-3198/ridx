import pysmile

from helper.hepler import generate_all_binary, get_attribute
from .node import (NODE_CPT, NODE_CPT_TRUE, Node, NodeCPT,
                   NodeDecision, NODE_CPT_FALSE)

pysmile.License((
    b"SMILE LICENSE fe8529b2 a1ee03b3 8fde335e "
    b"THIS IS AN ACADEMIC LICENSE AND CAN BE USED "
    b"SOLELY FOR ACADEMIC RESEARCH AND TEACHING, "
    b"AS DEFINED IN THE BAYESFUSION ACADEMIC "
    b"SOFTWARE LICENSING AGREEMENT. "
    b"Serial #: 23zu22fl5ajyflgah4637l2t "
    b"Issued for: Hieu Hoang (hieu.jno1@gmail.com) "
    b"Academic institution: hanoi university of science and technology "
    b"Valid until: 2022-11-07 "
    b"Issued by BayesFusion activation server"
), [
    0x02, 0x73, 0x81, 0x62, 0xa4, 0x0d, 0xb0, 0x70, 0x59, 0xdd, 0xf3, 0x6a, 0xd4, 0xbf, 0xec, 0xd1,
    0xea, 0x17, 0xe8, 0x23, 0xf1, 0xa0, 0xbb, 0xdb, 0x22, 0x19, 0xbc, 0x14, 0x41, 0xc9, 0x2a, 0x6b,
    0xb3, 0x8d, 0xdc, 0xc4, 0x80, 0x58, 0xee, 0xe1, 0x18, 0x6e, 0xdf, 0xb2, 0x6b, 0xa8, 0x50, 0x35,
    0x4e, 0x47, 0xf5, 0xf3, 0xe7, 0x47, 0xfe, 0xc8, 0x34, 0x00, 0xc2, 0x97, 0xaa, 0x61, 0x0e, 0x0d
])

TYPE_ATTACKER = True
TYPE_CVE = False

E_CVSS = {
    'Unproven': 0.85,
    'Proof-of-Concept': 0.9,
    'Functional': 0.95,
    'High': 1.00,
    'Not Defined': 1.00,
}

RL_CVSS = {
    'Official Fix': 0.87,
    'Temporary Fix': 0.9,
    'Workaround': 0.95,
    'Unavailable': 1.00,
    'Not Defined': 1.00,
}

RC_CVSS = {
    'Unconfirmed': 0.90,
    'Uncorroborated': 0.95,
    'Confirmed': 1.00,
    'Not Defined': 1.00,
}


class INetwork:
    DECIMAL = 4
    DEFAULT_TIME_STEP = 2
    DEFAULT_TIME_LAYER = 2

    network: pysmile.Network
    nodes: dict
    base_impact: float
    base_benefit: float

    countermeasures: list
    attack_graph: dict
    vulnerabilities: list
    node_temporal: list
    assets: dict
    security_goals: list

    target: dict

    cia_metric: dict = {
        'confidentiality': {
            'NONE': 1,
            'PARTIAL': 2,
            'COMPLETE': 3,
        },
        'integrity': {
            'NONE': 1,
            'PARTIAL': 2,
            'COMPLETE': 3,
        },
        'availability': {
            'NONE': 1,
            'PARTIAL': 2,
            'COMPLETE': 3,
        }
    }

    exploitability: float
    remediation_level: float
    report_confidence: float

    # DBN
    time_step: int
    time_layer: int

    def __init__(self):
        pass

    def add_node(self, target: Node):
        if isinstance(target, NodeCPT):
            node = self.network.add_node(pysmile.NodeType.CPT, target.id)
            self.network.set_node_name(node, target.name)
            initial_outcome_count = self.network.get_outcome_count(node)
            for i in range(0, initial_outcome_count):
                self.network.set_outcome_id(node, i, target.outcomes[i])
            for i in range(initial_outcome_count, len(target.outcomes)):
                self.network.add_outcome(node, target.outcomes[i])
        elif isinstance(target, NodeDecision):
            node = self.network.add_node(pysmile.NodeType.DECISION, target.id)
            self.network.set_node_name(node, target.name)
            initial_outcome_count = self.network.get_outcome_count(node)
            for i in range(0, initial_outcome_count):
                self.network.set_outcome_id(node, i, target.outcomes[i])
            for i in range(initial_outcome_count, len(target.outcomes)):
                self.network.add_outcome(node, target.outcomes[i])
        else:
            raise Exception('add_node failed')
        target.handle = node
        self.nodes[node] = target
        return node

    def set_node_temporal_type(self, node_handle: int):
        if isinstance(self.nodes[node_handle], NodeCPT):
            if not self.nodes[node_handle].is_attacker:
                self.network.set_node_temporal_type(node_handle, pysmile.NodeTemporalType.PLATE)

    def get_outcome_id(self, node_handle: int, outcome_index: int):
        self.network.get_outcome_id(node_handle, outcome_index)

    def add_link(self, parent_node: Node, child_node: Node):
        self.network.add_arc(parent_node.id, child_node.id)

    def set_node_definition(self, node_handle: int, definition: list):
        self.network.set_node_definition(node_handle, definition)

    def set_node_temporal_definition(self, node_handle, def_temporal):
        self.network.set_node_temporal_definition(node_handle, self.time_layer, def_temporal)

    def _set_new_probability(self, node_handle: int, init_coverage: dict):
        target = self.nodes[node_handle]
        coverage_all = 0
        if isinstance(target, NodeCPT):
            name = target.name
            index = False
            for init_coverage_name in init_coverage:
                if init_coverage_name in name:
                    index = init_coverage_name
                    break
            if index:
                coverage = init_coverage[index]
                if len(coverage) == 1:
                    coverage_all = coverage[0]
                elif len(coverage) > 1:
                    _coverage = 1
                    for tmp in coverage:
                        _coverage *= (1 - tmp)
                    coverage_all = 1 - _coverage
                target.new_probability = round(target.probability * (1 - coverage_all), INetwork.DECIMAL)
        else:
            raise Exception('Not cpt node')

    def get_posteriors(self, node_handle: int):
        target = self.nodes[node_handle]
        name = self.nodes[node_handle].name
        if isinstance(target, NodeCPT):
            result = {}
            if self.network.get_node_temporal_type(node_handle) == pysmile.NodeTemporalType.PLATE:
                outcome_count = self.network.get_outcome_count(node_handle)
                v = self.network.get_node_value(node_handle)
                outcomes = []
                for step in range(0, self.time_step):
                    outcome_step = {
                        NODE_CPT_TRUE: round(v[step * outcome_count], INetwork.DECIMAL)
                    }
                    outcome_step[NODE_CPT_FALSE] = round(1 - outcome_step[NODE_CPT_TRUE], INetwork.DECIMAL)
                    outcomes.append(outcome_step)
                return {
                    'name': name,
                    'is_evidence': False,
                    'type': NODE_CPT,
                    'outcomes': outcomes,
                    'time_step': self.time_step,
                }
            else:
                posteriors = self.network.get_node_value(node_handle)
                for i in range(0, len(posteriors)):
                    result[self.network.get_outcome_id(node_handle, i)] = round((posteriors[i]),
                                                                                INetwork.DECIMAL)
                return {
                    'name': name,
                    'is_evidence': False,
                    'type': NODE_CPT,
                    'outcomes': result,
                    'time_step': 1,
                }

    def _get_node_by_name(self, name):
        result = []
        for node_handle in self.nodes:
            if name in self.nodes[node_handle].name:
                result.append(node_handle)
        if len(result) != 0:
            return result
        return None

    def _update_network(self):
        self.network.update_beliefs()

    def _auto_set_node_definition(self, init_coverage: dict):
        for node_handle in self.nodes:
            if isinstance(self.nodes[node_handle], NodeCPT):
                self._set_new_probability(node_handle, init_coverage)
                parents = self.network.get_parents(node_handle)
                cpt = self._cpt(node_handle, parents)
                self.set_node_definition(node_handle, cpt)
        self._update_network()

    def _cpt(self, node_handle, parents):
        n = len(parents)
        probability = round(self.nodes[node_handle].new_probability, INetwork.DECIMAL)
        if n == 0:
            result = [probability, round(1 - probability, INetwork.DECIMAL)]
        else:
            arr = [None] * n
            l = []
            generate_all_binary(n, arr, 0, l)
            l.reverse()
            cpts = []
            for val in l:
                number_true = 0
                for i in val:
                    if i == 1:
                        number_true += 1
                if number_true == 0:
                    cpt = 0
                else:
                    cpt = 1 - pow(1 - probability, number_true)
                cpts += [round(cpt, INetwork.DECIMAL), round(1 - cpt, INetwork.DECIMAL)]
            result = cpts
        return result

    def get_all_posteriors(self):
        tmp_cpts = []
        cpts = []
        for node_handle in self.network.get_all_nodes():
            posterior = self.get_posteriors(node_handle)
            if posterior['type'] == NODE_CPT:
                tmp_cpts.append(posterior)
        for cpt in tmp_cpts:
            if 'Attacker_' in cpt['name']:
                cpts.append({
                    **cpt,
                    'name': cpt['name'].replace('Attacker_', ''),
                    'is_attacker': True
                })
            else:
                cpts.append({
                    **cpt,
                    'name': cpt['name'].replace('Vulnerability_', ''),
                    'is_attacker': False
                })

        return cpts + self.get_decisions()

    def _get_countermeasure(self, cve_name: str):
        counter = []
        for countermeasure in self.countermeasures:
            if cve_name in countermeasure['cover_cves']:
                counter.append(countermeasure)
        return counter

    def _init_coverage(self):
        result = {}
        for tmp in self.attack_graph['nodes']:
            if tmp['is_attacker'] == TYPE_CVE:
                countermeasures = self._get_countermeasure(tmp['cve_id'])
                if len(countermeasures) != 0:
                    if tmp['cve_id'] not in result:
                        result[tmp['cve_id']] = [c['coverage'] for c in countermeasures]
        return result

    # attack_graph: dict, countermeasures: list, vulnerabilities: list, base_impact: float = 100,
    # base_benefit: float = 100, time_step: int = DEFAULT_TIME_STEP,
    # time_layer: int = DEFAULT_TIME_LAYER

    def _parser_vulnerabilities(self, vulnerabilities):
        tmp = {}
        for asset in vulnerabilities:
            cves = []
            for vul in asset['cves']:
                cves.append({
                    **vul,
                    'exploitabilityScore': get_attribute(vul, 'impact.baseMetricV2.exploitabilityScore') / 10.0,
                    'impactScore': get_attribute(vul, 'impact.baseMetricV2.impactScore') / 10.0,
                    'confidentialityImpact': get_attribute(vul, 'impact.baseMetricV2.cvssV2.confidentialityImpact'),
                    'integrityImpact': get_attribute(vul, 'impact.baseMetricV2.cvssV2.integrityImpact'),
                    'availabilityImpact': get_attribute(vul, 'impact.baseMetricV2.cvssV2.availabilityImpact'),
                })
            tmp[asset['asset_id']] = cves
        self.vulnerabilities = tmp

    def _parser_assets(self, assets):
        self.assets = {}
        for asset in assets:
            self.assets[asset['id']] = {
                **asset,
                'cve_nodes': []
            }

    def get_cia_assets(self):
        results = []
        for asset_id in self.assets:
            results.append(self.__get_cia_asset(asset_id))
        return results

    def get_likelihood(self):
        for handle in self.nodes:
            node = self.nodes[handle]
            if not node.is_attacker:
                if node.cve_id == self.target['cve_id'] and node.asset_id == self.target['asset_id']:
                    return self.get_posteriors(handle)
        return None

    def __get_cia_asset(self, asset_id):
        results = {
            'id': asset_id,
            'name': self.assets[asset_id]['name'],
            'confidentiality': [],
            'integrity': [],
            'availability': [],
            'cia': [],
        }
        cve_nodes = self.assets[asset_id]['cve_nodes']
        asset_confidentiality = 0
        asset_integrity = 0
        asset_availability = 0

        if self.time_layer == 1:
            for node in cve_nodes:
                probability = self.get_posteriors(node.handle)['outcomes'][NODE_CPT_TRUE]
                cve = next((x for x in self.vulnerabilities[asset_id] if x['cve_id'] == node.cve_id), None)
                print(node.cve_id, probability, self.cia_metric['confidentiality'][cve['confidentialityImpact']],
                      self.cia_metric['integrity'][cve['integrityImpact']],
                      self.cia_metric['availability'][cve['availabilityImpact']])
                asset_confidentiality += self.cia_metric['confidentiality'][cve['confidentialityImpact']] * probability
                asset_integrity += self.cia_metric['integrity'][cve['integrityImpact']] * probability
                asset_availability += self.cia_metric['availability'][cve['availabilityImpact']] * probability

            c = 3
            i = 3
            a = 3

            if len(cve_nodes) != 0:
                c = round(3 - asset_confidentiality / len(cve_nodes), INetwork.DECIMAL)
                i = round(3 - asset_integrity / len(cve_nodes), INetwork.DECIMAL)
                a = round(3 - asset_availability / len(cve_nodes), INetwork.DECIMAL)

            return {
                **results,
                'confidentiality': c,
                'integrity': i,
                'availability': a,
                'cia': round(c + i + a, INetwork.DECIMAL),
            }

        for k in range(self.time_layer):
            asset_confidentiality = 0
            asset_integrity = 0
            asset_availability = 0
            for node in cve_nodes:
                if self.network.get_node_temporal_type(node.handle) == pysmile.NodeTemporalType.PLATE:
                    probability = self.get_posteriors(node.handle)['outcomes'][k][NODE_CPT_TRUE]
                else:
                    probability = self.get_posteriors(node.handle)['outcomes'][NODE_CPT_TRUE]
                cve = next((x for x in self.vulnerabilities[asset_id] if x['cve_id'] == node.cve_id), None)
                asset_confidentiality += self.cia_metric['confidentiality'][cve['confidentialityImpact']] * probability
                asset_integrity += self.cia_metric['integrity'][cve['integrityImpact']] * probability
                asset_availability += self.cia_metric['availability'][cve['availabilityImpact']] * probability
            c = 3
            i = 3
            a = 3

            if len(cve_nodes) != 0:
                c = round(3 - asset_confidentiality / len(cve_nodes), INetwork.DECIMAL)
                i = round(3 - asset_integrity / len(cve_nodes), INetwork.DECIMAL)
                a = round(3 - asset_availability / len(cve_nodes), INetwork.DECIMAL)

            results = {
                **results,
                'confidentiality': results['confidentiality'] + [c],
                'integrity': results['integrity'] + [i],
                'availability': results['availability'] + [a],
                'cia': results['cia'] + [round(c + i + a, INetwork.DECIMAL)],
            }
        return results
