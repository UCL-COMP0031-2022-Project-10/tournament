from datetime import datetime
from typing import List, Type

from tournament.action import Action
from tournament.agent import Agent, TrainableAgent
from tournament.match import Match


class Environment:
    def __init__(self) -> None:
        self.counts = {Action.COOPERATE: 0, Action.DEFECT: 0}

    def _play_training_match(
        self,
        trainee: TrainableAgent,
        opponent: Agent,
        continuation_probability: float,
        limit: int,
        noise: float,
    ):
        trainee.notify_prematch()

        for moves, scores, rewards in Match(trainee, opponent).play_moves(
            continuation_probability=continuation_probability,
            limit=limit,
            noise=noise,
        ):
            self.counts[moves[0]] += 1
            trainee.update(moves, scores, rewards)

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
        limit: int = 100000,
        noise: float = 0,
        repetitions: int = 1,
        epochs: int = 1,
    ) -> None:
        trainee.setup()

        print(f"[{datetime.now().strftime('%H:%M:%S')}] Commencement of training.")
        for i in range(epochs):
            self._play_epoch(
                trainee, continuation_probability, limit, noise, repetitions
            )
            print(
                f"[{datetime.now().strftime('%H:%M:%S')}] Completed epoch {i + 1}: {trainee.metric}"
            )

        trainee.teardown()
