# this class is renamed to RandomAgent to resolve the naming conflict

from random import choice, random
from typing import List

from tournament.action import Action
from tournament.agent import Agent


class RandomAgent(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        # Play a random action
        return choice([Action.COOPERATE, Action.DEFECT])


class Probabilistic(Agent):
    """
    This probablistic agent has a constant probability of cooperating after the opponent cooperates or defects.

    It was inspired by the following paper: Nowak, M.A. and Sigmund, K., 1992. Tit for tat in heterogeneous populations. Nature, 355(6357), pp.250-253.
    """

    def __init__(self) -> None:
        self.lb = 1
        self.p = {
            (Action.COOPERATE,): 0.5,
            (Action.DEFECT,): 0.5,
        }

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if len(history) < self.lb:
            return choice([Action.COOPERATE, Action.DEFECT])

        return (
            Action.COOPERATE
            if random() < self.p[tuple(opp_history[-self.lb :])]
            else Action.DEFECT
        )


class ProbabilisticLB1(Probabilistic):
    pass


class ProbabilisticLB2(Probabilistic):
    def __init__(self) -> None:
        self.lb = 2
        self.p = {
            (Action.COOPERATE, Action.COOPERATE): 0.5,
            (Action.COOPERATE, Action.DEFECT): 0.5,
            (Action.DEFECT, Action.COOPERATE): 0.5,
            (Action.DEFECT, Action.DEFECT): 0.5,
        }
