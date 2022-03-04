import random
from typing import List, Type

from tournament.agent import Agent, TrainableAgent
from tournament.environment import Environment


class MultipleRuleBasedAgentEnvironment(Environment):
    def __init__(self, agents: List[Type[Agent]]) -> None:
        super().__init__()

        self.agents = agents

    def _play_epoch(
        self,
        trainee: TrainableAgent,
        continuation_probability: float = 1,
        limit: int = 10000,
        noise: float = 0,
        repetitions: int = 1,
    ):
        for opponent in random.sample(self.agents, len(self.agents)):
            for _ in range(repetitions):
                self._play_training_match(
                    trainee, opponent(), continuation_probability, limit, noise
                )
