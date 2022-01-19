from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import List

from tqdm import tqdm

from tournament.agent import Agent
from tournament.match import Match


def _play_match(a, b, repetitions, continuation_probability, limit, noise):
    scores_a = []
    scores_b = []

    for _ in range(repetitions):
        score_a, score_b = Match(a(), b()).play(
            continuation_probability=continuation_probability,
            limit=limit,
            noise=noise,
        )

        scores_a.append(score_a)
        scores_b.append(score_b)

    return a, b, scores_a, scores_b


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
            futures = [
                executor.submit(
                    _play_match,
                    a,
                    b,
                    repetitions,
                    continuation_probability,
                    limit,
                    noise,
                )
                for a in self.agents
                for b in self.agents
            ]

            for future in tqdm(
                as_completed(futures),
                total=(len(self.agents) ** 2),
                unit="matches",
            ):
                a, b, scores_a, scores_b = future.result()
                scores[a].extend(scores_a)
                scores[b].extend(scores_b)

        return scores
