from random import random

from tournament.action import Action, flip_action
from tournament.agent import Agent

C, D = Action.COOPERATE, Action.DEFECT

PAYOFF_MATRIX = {
    (C, C): (3, 3),
    (C, D): (0, 5),
    (D, C): (5, 0),
    (D, D): (1, 1),
}


class Match:
    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2

    def _mutate(self, action: Action, noise: float):
        if 0 < random() < noise:
            return flip_action(action)

        return action

    def play_moves(self, continuation_probability: float, limit: int, noise: float):
        score1 = 0
        score2 = 0

        history1 = []
        history2 = []

        i = 0
        while i < limit and (i < 1 or random() < continuation_probability):
            move1 = self._mutate(self.agent1.play_move(history1, history2), noise)
            move2 = self._mutate(self.agent2.play_move(history2, history1), noise)

            increase1, increase2 = PAYOFF_MATRIX[(move1, move2)]
            score1 += increase1
            score2 += increase2

            history1.append(move1)
            history2.append(move2)

            i += 1
            yield (move1, move2), (score1, score2), (increase1, increase2)

    def play(
        self, continuation_probability: float = 1, limit: int = 10000, noise: float = 0
    ):
        *_, (moves, scores, rewards) = self.play_moves(
            continuation_probability=continuation_probability, limit=limit, noise=noise
        )
        return scores
