import pickle
from pprint import pprint

import pysmile
from typing import List

from core.bayes.helper.hepler import generate_all_binary, get_attribute
from core.bayes.model.node import (NODE_CPT, NODE_DECISION, NODE_DECISION_FALSE,
                        NODE_DECISION_TRUE, NODE_CPT_TRUE, Node, NodeCPT,
                        NodeDecision, NodeUtility, NODE_CPT_FALSE)

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


def get_utility_value(utility_table: list, prob: float):
    middle_index = len(utility_table) // 2
    vul_exploited = utility_table[:middle_index]
    vul_not_exploied = utility_table[middle_index:]
    utility_value = []
    for index in range(len(vul_exploited)):
        utility_value.append(vul_exploited[index] * prob + (1 - prob) * vul_not_exploied[index])
    return utility_value


def calculator_decision(utility_values: List[float], decisions: List[str]):
    result = {}
    middle_index = len(utility_values) // 2
    exploited = utility_values[:middle_index]
    not_exploited = utility_values[middle_index:]
    for decision in decisions:
        result[decision] = [max(exploited), max(not_exploited)]
        middle_index = len(exploited) // 2
        exploited = exploited[:middle_index]
        not_exploited = not_exploited[:middle_index]

    return result


exploitability_cvss  = {
    'Unproven': 0.85,
    'Proof-of-Concept': 0.9,
    'Functional': 0.95,
    'High': 1.00,
    'Not Defined': 1.00,
}

remediation_level_cvss = {
    'Official Fix': 0.87,
    'Temporary Fix': 0.9,
    'Workaround': 0.95,
    'Unavailable': 1.00,
    'Not Defined': 1.00,
}

report_confidence_cvss = {
    'Unconfirmed': 0.90,
    'Uncorroborated': 0.95,
    'Confirmed': 1.00,
    'Not Defined': 1.00,
}


class INetwork():
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
        elif isinstance(target, NodeUtility):
            node = self.network.add_node(pysmile.NodeType.UTILITY, target.id)
            self.network.set_node_name(node, target.name)
        else:
            raise Exception('add_node failed')
        target.handle = node
        self.nodes[node] = target
        return node

    def set_node_temporal_type(self, node_handle: int):
        if isinstance(self.nodes[node_handle], NodeCPT):
            if not self.nodes[node_handle].is_attacker:
                self.network.set_node_temporal_type(node_handle, pysmile.NodeTemporalType.PLATE)

    # def add_temporal_arc(self, node_handle: int):
    #     if self.nodes[node_handle].name.split('_')[1] in self.node_temporal:
    #         self.network.add_temporal_arc(node_handle, node_handle, self.time_layer)

    def get_outcome_id(self, node_handle: int, outcome_index: int):
        self.network.get_outcome_id(node_handle, outcome_index)


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
            # if self.network.is_evidence(node_handle):
            #     return {
            #         'name': name,
            #         'is_evidence': True,
            #         'evidence': self.network.get_outcome_id(node_handle, self.network.get_evidence(node_handle)),
            #         'type': NODE_CPT,
            #     }
            # else:
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
            # print(self.nodes[node_handle].name)
            if name in self.nodes[node_handle].name:
                result.append(node_handle)
        if len(result) != 0:
            return result
        return None

    def get_utility_value(self, countermeasure: dict):
        cover_cves = countermeasure['cover_cves']
        cost = countermeasure['cost']
        coverage = countermeasure['coverage']
        utility_true = 0
        utility_false = 0
        for cover_cve in cover_cves:
            node_handles = self._get_node_by_name("{}_".format(cover_cve))
            if not node_handles:
                continue
            for node_handle in node_handles:
                # TODO: BN cơ sở
                node = self.nodes[node_handle]
                prob = self.get_posteriors(node_handle)['outcomes'][NODE_CPT_TRUE]

                cost_benefit = self.base_benefit * coverage
                attack_damage = self.base_impact * node.impact

                utility_true += prob * (attack_damage + cost_benefit - cost) + (1 - prob) * (-cost)
                utility_false += prob * (- attack_damage)

        utility_true = round(utility_true, INetwork.DECIMAL)
        utility_false = round(utility_false, INetwork.DECIMAL)
        return {
            'name': countermeasure['name'],
            'type': NODE_DECISION,
            'outcomes': {
                NODE_DECISION_TRUE: utility_true,
                NODE_DECISION_FALSE: utility_false,
            },
            'cost': cost,
        }

    def _update_network(self):
        self.network.update_beliefs()

    def _auto_set_node_definition(self, init_coverage: dict):
        for node_handle in self.nodes:
            if isinstance(self.nodes[node_handle], NodeCPT):
                self._set_new_probability(node_handle, init_coverage)
                node = self.nodes[node_handle]
                # print(node.cve_id, node.probability, node.new_probability)
                parents = self.network.get_parents(node_handle)
                cpt = self._cpt(node_handle, parents)
                self.set_node_definition(node_handle, cpt)
        self._update_network()

    def _cpt(self, node_handle, parents):
        n = len(parents)
        probability = round(self.nodes[node_handle].new_probability, INetwork.DECIMAL)
        relation = self.nodes[node_handle].relation
        if n == 0:
            result = [probability, round(1 - probability, INetwork.DECIMAL)]
        else:
            if relation == NodeCPT.OR:
                arr = [None] * (n)
                l = []
                generate_all_binary(n, arr, 0, l)
                l.reverse()
                cpts = []
                # print('Bin', probability, len(parents), l)
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
            else:
                # TODO: Change AND
                result = [probability, round(1 - probability, INetwork.DECIMAL)] + [0, 1] * (pow(2, n) - 1)
        return result

    def get_utility(self, node_handle: int, layer: int = 0):
        node = self.nodes[node_handle]
        if isinstance(node, NodeCPT):
            if not node.is_attacker:
                result = {
                    'node': {},
                    'countermeasures': [],
                    'utility_table': [],
                    'utility_values': [],
                }
                countermeasures = self._get_countermeasure(node.name.split('_')[1])
                result['node'] = self.get_posteriors(node_handle)
                result['countermeasures'] = countermeasures

                if not self.network.get_node_temporal_type(node_handle) == pysmile.NodeTemporalType.PLATE:
                    __utility = self._get_utility(node, result['node']['outcomes'][NODE_CPT_TRUE], countermeasures)
                    return {
                        **result,
                        'utility_table': __utility[0],
                        'utility_values': __utility[1],
                    }
                else:
                    outcome = result['node']['outcomes'][layer]
                    __utility = self._get_utility(node, outcome[NODE_CPT_TRUE], countermeasures)
                    return {
                        **result,
                        'utility_table': __utility[0],
                        'utility_values': __utility[1],
                    }
        return {}

    def _get_utility(self, node, prob, countermeasures):
        attack_damage = self.base_impact * node.impact

        utility_table = []
        utility_values = []

        number_countermeasures = len(countermeasures)
        if number_countermeasures > 0:
            arr = [None] * number_countermeasures
            l = []
            generate_all_binary(number_countermeasures, arr, 0, l)
            l.reverse()
            # CVE khai thác
            for item in l:
                if item == [0] * number_countermeasures:
                    utility_table.append(-attack_damage)
                else:
                    utility_value = attack_damage

                    for index, value in enumerate(item):
                        if value:  # = 1
                            cost_benefit = self.base_benefit * countermeasures[index]['coverage']
                            cost = countermeasures[index]['cost']
                            utility_value = utility_value + cost_benefit - cost
                    utility_table.append(utility_value)
            # CVE khong bi khai thac
            for item in l:
                utility_value = 0
                for index, value in enumerate(item):
                    if value:  # = 1
                        cost = countermeasures[index]['cost']
                        utility_value = utility_value - cost
                utility_table.append(utility_value)
            utility_values = get_utility_value(utility_table, prob)
        return [utility_table, utility_values]

    def get_decisions(self):
        decisions = []
        for i in range(self.time_layer):
            decisions_layer = []
            decisions_cost = self.get_decision_cost(i)
            for index, countermeasure in enumerate(self.countermeasures):
                decisions_layer += [{
                    'id': index,
                    'name': countermeasure['name'],
                    'type': NODE_DECISION,
                    'outcomes': {
                        NODE_DECISION_TRUE: decisions_cost[countermeasure['name']][NODE_DECISION_TRUE],
                        NODE_DECISION_FALSE: decisions_cost[countermeasure['name']][NODE_DECISION_FALSE],
                    },
                    'cost': countermeasure['cost'],
                }]
            decisions.append(decisions_layer)
        if self.time_layer == 1:
            return decisions[0]

        result = []
        for k in decisions[0]:
            result.append({
                **k,
                'outcomes': [k['outcomes']]
            })
        for i in range(1, self.time_layer):
            d = decisions[i]
            for index in range(len(d)):
                result[index] = {
                    **result[index],
                    'outcomes': result[index]['outcomes'] + [d[index]['outcomes']]
                }

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

    def write_file(self, filename):
        if '.xdsl' not in filename:
            filename = filename + '.xdsl'
        self.network.write_file(filename)
        # print('Network written to', filename)

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

    def get_decision_cost(self, layer: int = 0):
        all_node_cves = []
        countermeasures_cost = {}
        for node_handle in self.nodes:
            tmp = self.get_utility(node_handle, layer)
            if len(tmp):
                all_node_cves.append(tmp)
        for node in all_node_cves:
            countermeasures_names = [target['name'] for target in node['countermeasures']]
            costs = calculator_decision(node['utility_values'], countermeasures_names)
            for target in costs:
                if target in countermeasures_cost:
                    countermeasures_cost[target] = {
                        NODE_DECISION_TRUE: round(countermeasures_cost[target][NODE_DECISION_TRUE] + costs[target][0],
                                                  INetwork.DECIMAL),
                        NODE_DECISION_FALSE: round(countermeasures_cost[target][NODE_DECISION_FALSE] + costs[target][1],
                                                   INetwork.DECIMAL),
                    }
                else:
                    countermeasures_cost[target] = {
                        NODE_DECISION_TRUE: round(costs[target][0], INetwork.DECIMAL),
                        NODE_DECISION_FALSE: round(costs[target][1], INetwork.DECIMAL),
                    }
        for countermeasure in self.countermeasures:
            if countermeasure['name'] not in countermeasures_cost:
                countermeasures_cost[countermeasure['name']] = {
                    NODE_DECISION_TRUE: - countermeasure['cost'],
                    NODE_DECISION_FALSE: 0,
                }
        return countermeasures_cost

    # attack_graph: dict, countermeasures: list, vulnerabilities: list, base_impact: float = 100,
    # base_benefit: float = 100, time_step: int = DEFAULT_TIME_STEP,
    # time_layer: int = DEFAULT_TIME_LAYER
    def dump(self):
        dump_attr = {
            'attack_graph': self.attack_graph,
            'countermeasures': self.countermeasures,
            'vulnerabilities': self.vulnerabilities,
            'base_impact': self.base_impact,
            'base_benefit': self.base_benefit,
            'time_step': self.time_step,
            'time_layer': self.time_layer,
        }
        return pickle.dumps(dump_attr, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self, script):
        return pickle.loads(script)

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
                print(node.cve_id, probability, self.cia_metric['confidentiality'][cve['confidentialityImpact']], self.cia_metric['integrity'][cve['integrityImpact']], self.cia_metric['availability'][cve['availabilityImpact']])
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
                # print(node.cve_id, probability)
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