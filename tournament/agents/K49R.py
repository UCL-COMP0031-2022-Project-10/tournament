from typing import List
from tournament.action import Action
from tournament.agent import Agent
from random import random

class K49R(Agent):

    def __init__(self) -> None:
        pass

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:

        '''
            First, check if opponent is overly defective and defect if found. I.e., if they meet any of the following conditions:
            - turn > 39 and % defects > 0.39
            - turn > 29 and % defects > 0.65
            - turn > 19 and % defects > 0.79

            Else, cooperate if they cooperated last turn. If enemy defected, then either defect if opp has defected > 18 times or 50/50 chance.
            Note, cooperate on first move.
        '''
        
        if not history:
            return Action.COOPERATE

        num_defects = opp_history.count(Action.DEFECT)
        percent_defect = num_defects / len(opp_history)
        if len(history) > 39 and percent_defect > 0.39:
            return Action.DEFECT
        if len(history) > 29 and percent_defect > 0.65:
            return Action.DEFECT
        if len(history) > 19 and percent_defect > 0.79:
            return Action.DEFECT 

        if opp_history[-1] == Action.DEFECT:
            if num_defects > 18:
                return Action.DEFECT
            if random() < 0.5:
                return Action.DEFECT
        
        return Action.COOPERATE