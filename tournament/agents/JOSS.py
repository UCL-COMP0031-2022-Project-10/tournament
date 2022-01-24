from random import random
from typing import List

from tournament.agent import Action
from tournament.agent import Agent

class Joss(Agent):

    def play_move(self, history: List[Agent], opp_history: List[Agent]) -> Action:

        if not history:
            return Action.DEFECT

        if opp_history[-1] == Action.DEFECT:
            # always defect if opp defects
            return Action.DEFECT
        
        if random() <= 0.9:
            # if opp has cooperated, cooperate with 90% probability.
            return Action.COOPERATE
        return Action.DEFECT
