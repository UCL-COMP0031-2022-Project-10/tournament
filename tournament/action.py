from enum import Enum


class Action(Enum):
    COOPERATE = 1
    DEFECT = 2


def flip_action(action: Action):
    """Flips an action from COOPERATE to DEFECT and vice versa.

    Args:
        action (Action): COOPERATE or DEFECT

    Returns:
        Action: DEFECT or COOPERATE
    """

    return Action.COOPERATE if action is Action.DEFECT else Action.DEFECT
