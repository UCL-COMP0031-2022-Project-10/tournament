from datetime import datetime
from typing import List, Type

from tournament.action import Action
from tournament.agent import Agent, TrainableAgent
from tournament.match import Match


class Environment:
    def __init__(self, silent: bool = False) -> None:
        self.silent = silent
        self.counts = {Action.COOPERATE: 0, Action.DEFECT: 0}
        self.epoch_count = {Action.COOPERATE: 0, Action.DEFECT: 0}
        self.epoch_counts = []
        self.normalised_epoch_counts = []
        self.rewards = []
        self.metric_history = []

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
            self.epoch_count[moves[0]] += 1
            self.rewards.append(rewards[0])

            trainee.update(moves, scores, rewards)

        trainee.notify_postmatch()
        self.metric_history.append(trainee.metric)

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

        if not self.silent:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Commencement of training.")

        for i in range(epochs):
            self.epoch_count = {Action.COOPERATE: 0, Action.DEFECT: 0}

            self._play_epoch(
                trainee, continuation_probability, limit, noise, repetitions
            )

            s = sum(self.epoch_count.values())
            self.epoch_counts.append(self.epoch_count)
            self.normalised_epoch_counts.append(
                {a: self.epoch_count[a] / s for a in self.epoch_count}
            )

            if not self.silent:
                print(
                    f"[{datetime.now().strftime('%H:%M:%S')}] Completed epoch {i + 1}: {trainee.metric}"
                )

        trainee.teardown()
