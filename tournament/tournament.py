from concurrent.futures import ProcessPoolExecutor
from typing import List

from tournament.agent import Agent
from tournament.match import Match


def _play_match(x):
    scores_a = []
    scores_b = []

    for _ in range(x[2]):
        score_a, score_b = Match(x[0](), x[1]()).play(
            continuation_probability=x[3],
            limit=x[4],
            noise=x[5],
        )

        scores_a.append(score_a)
        scores_b.append(score_b)

    return x[0], x[1], scores_a, scores_b


class RoundRobinTournament:
    def __init__(self, agents: List[Agent]) -> None:
        self.agents = agents

    def play(
        self,
        continuation_probability: float = 1,
        limit: int = 10000,
        noise: float = 0,
        repetitions: int = 1,
        jobs: int = 1,
    ):
        scores = {agent: [] for agent in self.agents}
        with ProcessPoolExecutor(max_workers=jobs) as executor:
            for a, b, scores_a, scores_b in executor.map(
                _play_match,
                [
                    (a, b, repetitions, continuation_probability, limit, noise)
                    for a in self.agents
                    for b in self.agents
                ],
            ):
                scores[a].extend(scores_a)
                scores[b].extend(scores_b)

        return scores
