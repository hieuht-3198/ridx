# from enum import IntEnum

# from typing import List

# class Priv(IntEnum):
#     OS_ADMIN = 10
#     OS_USER = 9
#     APP_ADMIN = 8
#     APP_USER = 7
#     NONE = 1


# class Av(IntEnum):
#     PHYSICAL = 5
#     LOCAL = 4
#     ADJACENT = 3
#     NETWORK = 2


# class Vulnerability:
#     name: str
#     pre_priv: Priv
#     post_priv: Priv
#     av: Av

#     def __init__(self, name: str, pre_priv: Priv, post_priv: Priv, av: Av) -> None:
#         self.name = name
#         self.pre_priv = pre_priv
#         self.post_priv = post_priv
#         self.av = av

# vul_1 = Vulnerability('vul1', Priv.NONE, Priv.OS_USER, Av.NETWORK)
# vul_2 = Vulnerability('vul2', Priv.OS_USER, Priv.OS_USER, Av.NETWORK)
# vul_3 = Vulnerability('vul3', Priv.NONE, Priv.OS_USER, Av.NETWORK)
# vul_4 = Vulnerability('vul4', Priv.OS_USER, Priv.OS_USER, Av.LOCAL)
# vul_5 = Vulnerability('vul5', Priv.NONE, Priv.OS_ADMIN, Av.ADJACENT)


# class Node:
#     name: str
#     priv: Priv
#     av: Av
#     reachable_nodes: list = []
#     vuls: List[Vulnerability] = []

#     def __init__(self, name: str) -> None:
#         self.name = name

# matrix_com = [
#     {
#         'source': 'device1',
#         'target': 'device2',
#         'priv': Priv.NONE,
#         'av': Av.NETWORK,
#     },
#     {
#         'source': 'device1',
#         'target': 'device3',
#         'priv': Priv.APP_USER,
#         'av': Av.NETWORK,
#     },
#     {
#         'source': 'device2',
#         'target': 'device3',
#         'priv': Priv.APP_ADMIN,
#         'av': Av.NETWORK,
#     },
#     {
#         'source': '*',
#         'target': 'device1',
#         'priv': Priv.APP_USER,
#         'av': Av.NETWORK,
#     },
# ]


# attacker_1 = Node('attacker1')
# attacker_1.priv = Priv.NONE
# attacker_1.av = Av.NETWORK

# device_1 = Node('device1')
# vuls_1 = [vul_1, vul_3, vul_5]
# vuls_1.sort(key= lambda x: (x.attack_vector, x.pre_condition, x.post_condition))
# device_1.vuls = vuls_1

# device_2 = Node('device2')
# vuls_2 = [vul_1, vul_2, vul_4, vul_3, vul_5]
# vuls_2.sort(key= lambda x: (x.attack_vector, x.pre_condition, x.post_condition))
# device_2.vuls = vuls_2

# device_3 = Node('device3')
# vuls_3 = [vul_2, vul_3, vul_5]
# vuls_3.sort(key= lambda x: (x.attack_vector, x.pre_condition, x.post_condition))
# device_3.vuls = vuls_3

# attackers = [attacker_1]

# attacker_1.reachable_nodes = [device_1, device_2]
# device_1.reachable_nodes = [device_2, device_3]
# device_2.reachable_nodes = [device_3]


# graph_edges = []
# graph_nodes = []

# def probe_asset(attacker: Node, asset: Node, vuls: List[Vulnerability]):
#     tmp_vuls = vuls[:]
#     while len(tmp_vuls) != 0:
#         vul = tmp_vuls.pop(0)
#         if attacker.av >= vul.av:
#             if vul.pre_priv == Priv.NONE or attacker.priv >= vul.pre_priv:
#                 source = attacker.name
#                 target = "{}_{}".format(asset.name, vul.name)
#                 edge = {
#                     'target': target,
#                     'source': source,
#                     'vul': vul,
#                 }
#                 if edge not in graph_edges:
#                     graph_edges.append(edge)
#                     print("--> {} -> {}".format(source, target))
#                 if source not in graph_nodes:
#                     graph_nodes.append(source)
#                 if target not in graph_nodes:
#                     graph_nodes.append(target)

#                 if attacker.priv < vul.post_priv:
#                     attacker.priv = vul.post_priv
#                 new_vuls = tmp_vuls
#                 new_asset = asset
#                 new_attacker = Node("{}_{}".format(asset.name, vul.name))
#                 new_attacker.priv = vul.post_priv
#                 new_attacker.av = attacker.av
#                 probe_asset(new_attacker, new_asset, new_vuls)


# def check_access(asset: Node, reachable_node: Node):
#     av = None
#     priv = None
#     for com in matrix_com:
#         if com['target'] == reachable_node.name and com['source'] == asset.name:
#             av = com['av']
#             priv = com['priv']
#             break
#     def find_vul(target, asset) -> Vulnerability:
#         for vul in asset.vulnerabilities:
#             if target == vul.name:
#                 return vul
#         return None

#     for graph_node in graph_nodes:
#         if '_' in graph_node:
#             if asset.name in graph_node:
#                 vul = find_vul(graph_node.split('_')[1], asset)
#                 if vul.post_priv >= priv:
#                     return [vul, priv, av]    
#     return [None, None, None]

# while len(attackers) != 0:
#     attacker = attackers.pop(0)
#     for node in attacker.reachable_nodes:
#         print(attacker.name, ' -> ', node.name, [vul.name for vul in node.vulnerabilities])
#         probe_asset(attacker, node, node.vulnerabilities)
#         print('-------------------')
#         for reachable_node in node.reachable_nodes:
#             vul, new_priv, new_av = check_access(node, reachable_node)
#             if new_priv:
#                 new_attacker = Node("{}_{}".format(node.name, vul.name))
#                 new_attacker.priv = new_priv
#                 new_attacker.av = new_av
#                 new_attacker.reachable_nodes = [reachable_node]
#                 attackers.append(new_attacker)
#     print('Len: ', len(attackers))

# print(graph_nodes)
    












