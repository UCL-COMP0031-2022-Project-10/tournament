from typing import List

from tournament.action import Action
from tournament.agent import Agent
from tournament.rtsp_list import rtsp_list


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
