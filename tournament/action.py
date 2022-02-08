from enum import Enum
from random import choice


class Action(Enum):
    COOPERATE = 0
    DEFECT = 1


def flip_action(action: Action):
    """Flips an action from COOPERATE to DEFECT and vice versa.

    Args:
        action (Action): COOPERATE or DEFECT

    Returns:
        Action: DEFECT or COOPERATE
    """

    return Action.COOPERATE if action is Action.DEFECT else Action.DEFECT


def random_action():
    return choice([Action.COOPERATE, Action.DEFECT])
