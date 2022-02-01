from typing import List, Type

from tournament.agent import Agent, TrainableAgent
from tournament.environment import Environment
from tournament.match import Match


class Environment:
    def __init__(self) -> None:
        pass

    def _play_training_match(
        self,
        trainee: TrainableAgent,
        opponent: Agent,
        continuation_probability: float,
        limit: int,
        noise: float,
    ):
        trainee.notify_prematch()

        for moves, scores in Match(trainee, opponent).play_moves(
            continuation_probability=continuation_probability,
            limit=limit,
            noise=noise,
        ):
            trainee.update(moves, scores)

        trainee.notify_postmatch()

    def _play_epoch(
        self,
        trainee: TrainableAgent,
        continuation_probability: float = 1,
        limit: int = 10000,
        noise: float = 0,
        repetitions: int = 1,
    ):
        raise NotImplementedError()

    def train(
        self,
        trainee: TrainableAgent,
        continuation_probability: float = 1,
        limit: int = 10000,
        noise: float = 0,
        repetitions: int = 1,
        epochs: int = 1,
    ) -> None:
        trainee.setup()

        for _ in range(epochs):
            self._play_epoch(
                trainee, continuation_probability, limit, noise, repetitions
            )

        trainee.teardown()
