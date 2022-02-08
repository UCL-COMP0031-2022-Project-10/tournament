from typing import List

from tournament.action import Action
from tournament.agent import Agent


class Pavlov(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        # Cooperate initially
        if not opp_history:
            return Action.COOPERATE

        return Action.COOPERATE if history[-1] == opp_history[-1] else Action.DEFECT
