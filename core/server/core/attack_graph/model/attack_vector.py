

from enum import IntEnum


class AttackVector(IntEnum):
    PHYSICAL = 5
    LOCAL = 4
    ADJACENT_NETWORK = 3
    NETWORK = 2

    NONE = 1