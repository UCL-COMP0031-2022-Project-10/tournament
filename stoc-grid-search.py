import itertools
from datetime import datetime

import pandas as pd

from tournament.action import Action
from tournament.agents.agents import AGENTS
from tournament.agents.constant import AllC, AllD
from tournament.agents.q_learning.dqn import DeepQLearner
from tournament.agents.random import Probabilistic, ProbabilisticLB2
from tournament.agents.tft import OmegaTFT, TitForTat
from tournament.gridsearch import evaluate
from tournament.tournament import RoundRobinTournament


def evaluate_stoc(cls, **kwargs):
    agent = cls(**kwargs)

    tournament = RoundRobinTournament(AGENTS, [agent])
    scores, times = tournament.play(
        continuation_probability=0.99654, repetitions=5, jobs=12
    )
    results = {agent: sum(scores[agent]) / len(scores[agent]) for agent in scores}

    return {
        **kwargs,
        "tn_rank": sorted(results, key=results.get, reverse=True).index(cls) + 1,
        "tn_mean_score": results[cls],
        "tn_mean_time": sum(times[cls]),
    }


class StocTest(ProbabilisticLB2):
    def __init__(self, p_cc, p_cd, p_dc, p_dd):
        super().__init__()

        self.p = {
            (Action.COOPERATE, Action.COOPERATE): p_cc,
            (Action.COOPERATE, Action.DEFECT): p_cd,
            (Action.DEFECT, Action.COOPERATE): p_dc,
            (Action.DEFECT, Action.DEFECT): p_dd,
        }


def main():
    agents = [TitForTat, OmegaTFT, AllC, AllD]

    grid = {
        "p_cc": [0, 0.25, 0.5, 0.75, 1],
        "p_cd": [0, 0.25, 0.5, 0.75, 1],
        "p_dc": [0, 0.25, 0.5, 0.75, 1],
        "p_dd": [0, 0.25, 0.5, 0.75, 1],
    }

    results = []
    try:
        space = list(itertools.product(*grid.values()))
        size = len(space)
        for i, hyperparameters in enumerate(space):
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} | {i + 1}/{size}]",
                *hyperparameters,
                sep="\t",
            )
            results.append(
                evaluate_stoc(StocTest, **dict(zip(grid.keys(), hyperparameters)))
            )
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} | {i + 1}/{size}]",
                f"RANK={results[-1]['tn_rank']}",
                f"SCORE={results[-1]['tn_mean_score']}",
                sep="\t",
            )
    except Exception as e:
        print("Quitting evaluation early.", str(e))

    if results:
        df = pd.DataFrame(results)
        df["agents"] = ",".join([a.__name__ for a in agents])
        df.to_csv(f"results/stoc-2-{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.csv")


if __name__ == "__main__":
    main()
