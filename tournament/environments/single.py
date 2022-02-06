from typing import List, Type

from tournament.agent import Agent, TrainableAgent
from tournament.environment import Environment


class SingleRuleBasedAgentEnvironment(Environment):
    def __init__(self, opponent: Type[Agent]) -> None:
        super().__init__()

        self.opponent = opponent

    def _play_epoch(
        self,
        trainee: TrainableAgent,
        continuation_probability: float = 1,
        limit: int = 10000,
        noise: float = 0,
        repetitions: int = 1,
    ):
        for _ in range(repetitions):
            self._play_training_match(
                trainee, self.opponent(), continuation_probability, limit, noise
            )
