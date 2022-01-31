from typing import List
from tournament.agent import Agent
from tournament.action import Action
from random import random

class K44R(Agent):

    def __init__(self) -> None:

        pass

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:

        '''
            Count # of defects, label it c_defect
            if c_defect equals 4, 7, or 9 => defect.
            if c_defect > 9 => defect after opponent defection with prob 0.5 ^(c_defect - 1). Otherwise, cooperate.
        '''

        c_defect = opp_history.count(Action.DEFECT)

        if c_defect == 4 or c_defect == 7 or c_defect == 9:
            return Action.DEFECT
        
        if opp_history[-1] == Action.DEFECT and c_defect > 9:
            if random() <= 0.5 ** (c_defect - 1):
                return Action.DEFECT
        
        return Action.COOPERATE