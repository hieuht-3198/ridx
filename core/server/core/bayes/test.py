from enum import IntEnum
from re import S

from typing import List


class Priv(IntEnum):
    OS_ADMIN = 10
    OS_USER = 9
    APP_ADMIN = 8
    APP_USER = 7
    NONE = 0


class Av(IntEnum):
    PHYSICAL = 5
    LOCAL = 4
    ADJACENT = 3
    NETWORK = 2


class Vulnerability:
    name: str
    pre_priv: Priv
    post_priv: Priv
    av: Av

    def __init__(self, name: str, pre_priv: Priv, post_priv: Priv, av: Av) -> None:
        self.name = name
        self.pre_priv = pre_priv
        self.post_priv = post_priv
        self.av = av


class Asset:
    name: str
    vulnerabilities: List[Vulnerability] = []
    reachable_assets: list = []
    priv: Priv
    av: Av

    def __init__(self, name: str) -> None:
        self.name = name

    def set_vulnerabilities(self, vul: List[Vulnerability]):
        tmp_vul = vul[:]
        tmp_vul.sort(key= lambda x: (x.pre_condition, x.post_condition))
        self.vulnerabilities = tmp_vul

class Attacker:
    name: str
    priv: Priv
    av: Av
    initial_assets: List[Asset]

    def __init__(self, name: str, priv: Priv, av: Av, initial_assets: List[Asset]) -> None:
        self.name = name
        self.priv = priv
        self.av = av
        self.initial_assets = initial_assets


def add_reachable_asset(node1: Asset, node2: Asset):
    if node2 not in node1.reachable_assets:
        node1.reachable_assets.append(node2)


class Node:
    name: str
    priv: Priv
    av: Av

    def __init__(self, name, priv: Priv, av: Av) -> None:
        self.name = name
        self.priv = priv
        self.av = av

vul_1 = Vulnerability('vul1', Priv.NONE, Priv.OS_USER, Av.NETWORK)
vul_2 = Vulnerability('vul2', Priv.OS_USER, Priv.OS_USER, Av.NETWORK)
vul_3 = Vulnerability('vul3', Priv.OS_ADMIN, Priv.OS_ADMIN, Av.NETWORK)
vul_4 = Vulnerability('vul4', Priv.OS_USER, Priv.OS_ADMIN, Av.LOCAL)
vul_5 = Vulnerability('vul5', Priv.NONE, Priv.OS_ADMIN, Av.ADJACENT)


device_1 = Asset('device_1')
device_1.set_vulnerabilities([vul_1, vul_2, vul_3])
device_2 = Asset('device_2')
device_2.set_vulnerabilities([vul_1, vul_5, vul_4])

add_reachable_asset(device_1, device_2)

attacker_1 = Attacker('attacker_1', Priv.NONE, Av.NETWORK, [device_1, device_2])

attackers = [attacker_1]

nodes = []
for attacker in attackers:
    node = Node(attacker.name, attacker.priv, attacker.av)

def print_edge(source, target):
    print("{} -> {}".format(source, target))


def probe(source: str, priv: Priv, av: Av, target_asset: str, vuls: List[Vulnerability]):
    current_priv = priv
    current_av = av
    for index, vul in enumerate(vuls):
        if vul.pre_priv == Priv.NONE or current_priv >= vul.pre_priv:
            print_edge(source, "{}_{}".format(vul.name, target_asset))
            if index == len(vuls):
                continue
            new_source = vul.name
            new_vuls = vuls[index+1:]
            new_priv = current_priv
            if vul.post_priv > current_priv:
                new_priv = vul.post_priv
            probe(new_source, new_priv, av, target_asset, new_vuls)
            continue

for attacker in attackers:
    for asset in attacker.initial_assets:
        print(asset.name)
        vuls = asset.vulnerabilities
        print([vul.name for vul in vuls])
        probe(attacker.name, attacker.priv, attacker.av, asset.name, asset.vulnerabilities)
