from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from itertools import chain
from typing import List, Type

from tqdm import tqdm

from tournament.agent import Agent
from tournament.match import Match


def _play_match(a, b, repetitions, continuation_probability, limit, noise):
    scores_a = []
    scores_b = []

    start = datetime.now()
    for _ in range(repetitions):
        score_a, score_b = Match(a(), b()).play(
            continuation_probability=continuation_probability,
            limit=limit,
            noise=noise,
        )

        scores_a.append(score_a)
        scores_b.append(score_b)
    end = datetime.now()

    return a, b, scores_a, scores_b, (end - start).total_seconds()


class RoundRobinTournament:
    def __init__(
        self, agents: List[Type[Agent]], instances: List[Agent] = None
    ) -> None:
        self.agents = agents
        self.instances = instances if instances else []

    def _play_multiprocessed_games(
        self, continuation_probability, limit, noise, repetitions, jobs
    ):
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

            for future in as_completed(futures):
                yield future.result()

    def play(
        self,
        continuation_probability: float = 1,
        limit: int = 10000,
        noise: float = 0,
        repetitions: int = 1,
        jobs: int = 1,
    ):
        scores = {agent: [] for agent in self.agents + self.instances}
        times = {agent: [] for agent in self.agents + self.instances}

        for a, b, scores_a, scores_b, time in tqdm(
            chain(
                self._play_multiprocessed_games(
                    continuation_probability, limit, noise, repetitions, jobs
                )
            ),
            total=((len(self.agents) + len(self.instances)) ** 2),
            unit="matches",
        ):
            scores[a].extend(scores_a)
            scores[b].extend(scores_b)

            times[a].append(time)
            times[b].append(time)

        return scores, times
