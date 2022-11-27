
from typing import List
from core.attack_graph.model.vulnerability import Vulnerability
from core.attack_graph.model.privilege import Privilege
from core.attack_graph.model.attack_vector import AttackVector
from core.attack_graph.model.node import Asset, Attacker

# import json
#
# f = open('sample.json')
# data = json.load(f)

convert_privilages = {
    'NONE': Privilege.NONE,
    'APP_USER': Privilege.APP_USER,
    'APP_ADMIN': Privilege.APP_ADMIN,
    'OS_USER': Privilege.OS_USER,
    'OS_ADMIN': Privilege.OS_ADMIN,
}

convert_attack_vectors = {
    'NETWORK': AttackVector.NETWORK,
    'ADJACENT_NETWORK': AttackVector.ADJACENT_NETWORK,
    'LOCAL': AttackVector.LOCAL,
    'PHYSICAL': AttackVector.PHYSICAL,
}


def __probe_asset(graph, attacker: Attacker, asset: Asset, vuls: List[Vulnerability]):
    tmp_vuls = vuls[:]
    while len(tmp_vuls) != 0:
        vul = tmp_vuls.pop(0)
        if attacker.attack_vector >= vul.attack_vector:
            if vul.pre_condition == Privilege.NONE or attacker.privilege >= vul.pre_condition:
                source = attacker.name
                target = f"{asset.name}_{vul.name}"
                edge = {
                    'target': target,
                    'source': source,
                    'vul': vul.name,
                }
                if edge not in graph['edges']:
                    graph['edges'].append(edge)
                    # print("--> {} -> {}".format(source, target))
                if source not in graph['nodes']:
                    graph['nodes'].append(source)
                if target not in graph['nodes']:
                    graph['nodes'].append(target)

                if attacker.privilege < vul.post_condition:
                    attacker.privilege = vul.post_condition
                new_vuls = tmp_vuls
                new_asset = asset
                new_attacker = Attacker(f"{asset.name}_{vul.name}")
                new_attacker.privilege = vul.post_condition
                new_attacker.attack_vector = attacker.attack_vector
                __probe_asset(graph, new_attacker, new_asset, new_vuls)


def __check_access_asset_to_asset(graph, asset: Asset, reachable_node: Asset):
    access_vector = None
    privilege = None
    for node in asset.reachable_nodes:
        if reachable_node.name == node['node'].name:
            access_vector = node['attack_vector']
            privilege = node['privilege']
            break

    def find_vul(target, asset) -> Vulnerability:
        for vul in asset.vulnerabilities:
            if target == vul.name:
                return vul
        return None

    for graph_node in graph['nodes']:
        if '_' in graph_node:
            if asset.name in graph_node:
                vul = find_vul(graph_node.split('_')[1], asset)
                if vul.post_condition >= privilege:
                    return [vul, privilege, access_vector]
    return [None, None, None]


def generator_attack_graph(deployment_scenario):
    graph = {
        'edges': [],
        'nodes': [],
    }

    assets = {}
    attackers = []
    for asset in deployment_scenario['cves']:
        tmp_asset = Asset(asset['asset_id'])
        vuls = []
        for cve in asset['cves']:
            vul = Vulnerability(
                name=cve['cve_id'],
                pre_condition=convert_privilages.get(cve['condition']['preCondition'], Privilege.NONE),
                post_condition=convert_privilages.get(cve['condition']['postCondition'], Privilege.NONE),
                attack_vector=convert_attack_vectors.get(cve['attack_vector'], AttackVector.NONE)
            )
            vuls.append(vul)
        tmp_asset.set_vulnerabilities(vuls)
        assets[asset['asset_id']] = tmp_asset

    for relationship in deployment_scenario['asset_relationships']:
        source = assets[relationship['source']]
        target = assets[relationship['target']]
        access_vector = convert_attack_vectors.get(relationship['access_vector'], AttackVector.NONE)
        privilege = convert_privilages.get(relationship['privilege'], Privilege.NONE)
        source.add_reachable_node(
            node=target,
            privilege=privilege,
            attack_vector=access_vector
        )

    for attacker in deployment_scenario['attackers']:
        tmp_attacker = Attacker(
            name=attacker['name'],
        )
        for target in attacker['targets']:
            target_asset = assets[target['asset_id']]
            privilege = convert_privilages.get(target['privilege'], Privilege.NONE)
            attack_vector = convert_attack_vectors.get(target['attack_vector'], AttackVector.NONE)
            tmp_attacker.add_reachable_node(
                node=target_asset,
                privilege=privilege,
                attack_vector=attack_vector
            )
        attackers.append(tmp_attacker)

    while len(attackers) != 0:
        # print('Attacker: ', len(attackers))
        attacker = attackers.pop(0)
        # print('Reachable nodes: ', len(attacker.reachable_nodes))
        for tmp_node in attacker.reachable_nodes:
            node = tmp_node['node']
            attacker.privilege = tmp_node['privilege']
            attacker.attack_vector = tmp_node['attack_vector']

            # print('Info', attacker.name, ' -> ', node.name, [vul.name for vul in node.vulnerabilities])
            __probe_asset(graph, attacker, node, node.vulnerabilities)
            # print('-------------------')
            for tmp_reachable_node in node.reachable_nodes:

                reachable_node = tmp_reachable_node['node']

                vul, new_priv, new_av = __check_access_asset_to_asset(graph, node, reachable_node)
                print(vul, new_priv, new_av)
                if new_priv:
                    new_attacker = Attacker(f"{node.name}_{vul.name}")
                    new_attacker.privilege = new_priv
                    new_attacker.attack_vector = new_av
                    new_attacker.reachable_nodes = [tmp_reachable_node]
                    attackers.append(new_attacker)

        # print('Attacker: ', len(attackers))

    return graph


# g= generator_attack_graph(data)
#
# import pydot
#
# def draw(parent_name, child_name):
#     edge = pydot.Edge(parent_name, child_name)
#     graph.add_edge(edge)
#
#
#
# graph = pydot.Dot(graph_type='digraph', rankdir='LR', nodesep = 0.25, ranksep=0.5)
# graph.set_node_defaults(shape='box')
#
# for edge in g['edges']:
#     draw(edge['source'], edge['target'])
#
#
# import tempfile
# from PIL import Image
# fout = tempfile.NamedTemporaryFile(suffix=".png")
# print(fout.name)
# graph.write('tmp.png',format="png")
# Image.open('tmp.png').show()