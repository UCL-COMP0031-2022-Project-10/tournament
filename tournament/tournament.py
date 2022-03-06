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
        score_a, score_b = Match(a, b).play(
            continuation_probability=continuation_probability,
            limit=limit,
            noise=noise,
        )

        scores_a.append(score_a)
        scores_b.append(score_b)
    end = datetime.now()

    return (
        type(a),
        type(b),
        scores_a,
        scores_b,
        (end - start).total_seconds(),
    )


def _play_multiprocessed_match(
    a, b, repetitions, continuation_probability, limit, noise
):
    return _play_match(a(), b(), repetitions, continuation_probability, limit, noise)


class RoundRobinTournament:
    def __init__(
        self, agents: List[Type[Agent]], instances: List[Agent] = None
    ) -> None:
        self.agents = agents
        self.instances = instances if instances is not None else []
        self.instance_types = [type(x) for x in self.instances]

    def _play_multiprocessed_games(
        self, continuation_probability, limit, noise, repetitions, jobs
    ):
        with ProcessPoolExecutor(max_workers=jobs) as executor:
            futures = [
                executor.submit(
                    _play_multiprocessed_match,
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

    def _play_sequential_games(self, cp, limit, noise, reps):
        for a in self.agents:
            for b in self.instances:
                yield _play_match(a(), b, reps, cp, limit, noise)

        for a in self.instances:
            for b in self.agents:
                yield _play_match(a, b(), reps, cp, limit, noise)

        for a in self.instances:
            for b in self.instances:
                yield _play_match(a, b, reps, cp, limit, noise)

    def play(
        self,
        continuation_probability: float = 1,
        limit: int = 10000,
        noise: float = 0,
        repetitions: int = 1,
        jobs: int = 1,
    ):
        scores = {agent: [] for agent in self.agents + self.instance_types}
        times = {agent: [] for agent in self.agents + self.instance_types}

        for a, b, scores_a, scores_b, time in tqdm(
            chain(
                self._play_multiprocessed_games(
                    continuation_probability, limit, noise, repetitions, jobs
                ),
                self._play_sequential_games(
                    continuation_probability, limit, noise, repetitions
                ),
            ),
            total=((len(self.agents) + len(self.instances)) ** 2),
            unit="matches",
        ):
            scores[a].extend(scores_a)
            scores[b].extend(scores_b)

            times[a].append(time)
            times[b].append(time)

        return scores, times
