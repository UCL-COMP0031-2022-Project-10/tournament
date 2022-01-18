from random import choice
from typing import List

from tournament.action import Action
from tournament.agent import Agent


class Random(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        # Play a random action
        return choice([Action.COOPERATE, Action.DEFECT])
