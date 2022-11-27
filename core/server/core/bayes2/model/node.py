NODE_CPT = 'NODE_CPT'
NODE_DECISION = 'NODE_DECISION'
NODE_TEMPORAL = 'NODE_TEMPORAL'

NODE_DECISION_TRUE = 'True'
NODE_DECISION_FALSE = 'False'

NODE_CPT_TRUE = 'True'
NODE_CPT_FALSE = 'False'

NODE_TEMPORAL_TRUE = 'True'
NODE_TEMPORAL_FALSE = 'False'


class Node:
    __id = 0
    handle: int
    id: str
    name: str
    outcomes: list = None

    def __init__(self, name) -> None:
        self.id = "Node_{}".format(Node.__id)
        self.name = name
        Node.__id += 1

    @classmethod
    def reset_id(cls):
        cls.__id = 0


class NodeDecision(Node):
    cost: float
    coverage: float

    def __init__(self, name, cost: float = 0, coverage: float = 0.5, outcomes=None) -> None:
        super().__init__(name)
        if outcomes is None:
            outcomes = [NODE_DECISION_TRUE, NODE_DECISION_FALSE]
        self.cost = cost
        self.outcomes = outcomes
        self.coverage = coverage


class NodeCPT(Node):
    probability: float
    new_probability: float
    impact: float = 1.0
    is_attacker: bool = False
    asset_id: str
    cve_id: str

    def __init__(self, name: str, probability: float = 1.0, impact: float = 1.0,
                 outcomes=None, asset_id=None, cve_id=None):
        if outcomes is None:
            outcomes = [NODE_CPT_TRUE, NODE_CPT_FALSE]
        if 0 <= probability <= 1:
            super().__init__(name)
            self.probability = probability
            self.new_probability = probability
            self.outcomes = outcomes
            self.impact = impact
            self.is_attacker = False
            self.asset_id = str(asset_id)
            self.cve_id = cve_id
        else:
            raise Exception('Probability invalid')

    def set_attacker(self):
        self.is_attacker = True
        self.cve_id = None
        self.asset_id = None
