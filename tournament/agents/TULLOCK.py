from typing import List
from random import random

from tournament.action import Action
from tournament.agent import Agent 

class Tullock(Agent):

    def play_move(self, history: List[Agent], opp_history: List[Agent]) -> Action:

        if len(history) <= 11:
            # always cooperate on first 11 moves.
            return Action.COOPERATE

        # 1) Calculate % of cooperate moves by opponent over the last 10 moves
        # 2) Tullock cooperates with probability (% of coop - 10). If % of coop < 0.1, defect.
        # % of cooperation moves by opp over the last 10 moves.
        percent_coop = opp_history[-10:].count(Action.COOPERATE) / 10
        if percent_coop <= 0.1:
            return Action.DEFECT
        
        if random() <= percent_coop - 10:
            return Action.COOPERATE
        return Action.DEFECT