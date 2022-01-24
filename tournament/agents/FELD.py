from typing import List
import random

from tournament.action import Action
from tournament.agent import Agent 

class Feld(Agent):

    def __init__(self):

        self._rate_of_dec = 1/200 # rate at which _prob_coop decreases
        self._prob_coop = 1 # probability of cooperating after a cooperation by opp.

    def play_move(self, history: List[Agent], opp_history: List[Agent]) -> Action:

        if opp_history[-1] == Action.DEFECT:
            # always defect if opp defected.
            return Action.DEFECT

        if len(history) < 200:
            # over a period of 200 moves, linearly decrease prob to 0.5.
            self._prob_coop -= self._rate_of_dec

        if random() <= self._prob_coop:
            # cooperate with probability self._prob_coop else defect
            return Action.COOPERATE
        return Action.DEFECT
