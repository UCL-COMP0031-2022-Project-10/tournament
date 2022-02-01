from typing import List

from tournament.action import Action
from tournament.agent import Agent


def rtsp_list(history: List[Action], opp_history: List[Action]) -> List[int]:
    result = []
    for actions in zip(history, opp_history):
        if actions == (Action.COOPERATE, Action.COOPERATE):
            result.append(0)
        elif actions == (Action.DEFECT, Action.COOPERATE):
            result.append(1)
        elif actions == (Action.COOPERATE, Action.DEFECT):
            result.append(2)
        else:
            result.append(3)
    return result


class Pavlov(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        # Cooperate initially
        if not opp_history:
            return Action.COOPERATE
        else:
            # previously the same choice, then COOPERATE
            previous = rtsp_list(history, opp_history)[-1]
            if previous == 0 or previous == 3:
                return Action.COOPERATE
            # previously different choice, then DEFECT
            else:
                return Action.DEFECT
