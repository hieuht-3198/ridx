

from typing import List
from core.attack_graph.model.attack_vector import AttackVector
from core.attack_graph.model.privilege import Privilege
from core.attack_graph.model.vulnerability import Vulnerability


class Node:
    name: str
    reachable_nodes: list

    def __init__(self, name) -> None:
        self.name = name
        self.reachable_nodes = []

    def add_reachable_node(self, node, privilege: Privilege, attack_vector: AttackVector):
        self.reachable_nodes.append({
            'node': node,
            'privilege': privilege,
            'attack_vector': attack_vector, 
        })


class Asset(Node):
    
    vulnerabilities: List[Vulnerability] = []

    def __init__(self, name) -> None:
        super().__init__(name)

    def set_vulnerabilities(self, vulnerabilities: List[Vulnerability]):
        self.vulnerabilities = vulnerabilities
        self.vulnerabilities.sort(key= lambda x: (x.attack_vector, x.pre_condition, x.post_condition))


class Attacker(Node):

    privilege: Privilege
    attack_vector: AttackVector

    def __init__(self, name) -> None:
        super().__init__(name)

