from typing import List

from tournament.action import Action
from tournament.agent import Agent


def rtsp_list(history: List[Action], opp_history: List[Action]) -> List[int]:
    return_list = []
    for i in range(len(history)):
        if history[i] == Action.COOPERATE and opp_history[i] == Action.COOPERATE:
            return_list.append(0)
        elif history[i] == Action.DEFECT and opp_history[i] == Action.COOPERATE:
            return_list.append(1)
        elif history[i] == Action.COOPERATE and opp_history[i] == Action.DEFECT:
            return_list.append(2)
        else:  # if(history[i] == Action.COOPERATE and opp_history[i] == Action.COOPERATE)
            return_list.append(3)
    return return_list


class Pavlov(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        # Cooperate initially
        if not opp_history:
            return Action.COOPERATE
        else:
            # previously same choice, then COOPERATE
            previous = rtsp_list(history, opp_history)[-1]
            if previous == 0 or previous == 3:
                return Action.COOPERATE
            # previously different choice, then DEFECT
            else:  # if rtsp_list[-1] == 1 or 2
                return Action.DEFECT
