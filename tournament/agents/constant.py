from random import choice
from typing import List

from tournament.action import Action
from tournament.agent import Agent


class AllC(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        return Action.COOPERATE


class AllD(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        return Action.DEFECT
