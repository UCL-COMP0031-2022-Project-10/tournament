import itertools
from datetime import datetime
from json import dumps

import numpy as np
import pandas as pd

from tournament.agents.q_learning.tabular import TabularQLearner
from tournament.agents.tft import (
    OmegaTFT,
    TitForTat,
    TFTT,
    TTFT,
    GenerousTFT,
    GradualTFT,
    )
from tournament.agents.axelrod_first import (
    Davis,
    Feld,
    Grudger,
    Joss,
    SteinAndRapoport,
    Tullock,
    Downing,
    Nydegger,
    TidemanAndChieruzzi,
    Grofman,
    Shubik
    )
from tournament.agents.random import RandomAgent
from tournament.agents.pavlov import Pavlov
from tournament.agents.axelrod_second import (
    Borufsen,
    Champion,
    Leyvraz,
    SecondByBlackK83R,
    SecondByGraaskampKatzen,
    SecondByHarrington,
    SecondByTidemanAndChieruzzi,
    SecondByWeiner,
    SecondByWhiteK72R,
    )
from tournament.agents.constant import AllC, AllD
from tournament.gridsearch import train_and_evaluate

class Tabular(TabularQLearner):
    def __init__(
        self,
        lookback,
        discount_rate,
        learning_rate,
        epsilon,
        epsilon_decay,
        decay_limit,
    ) -> None:
        super().__init__()

        self._lookback = lookback
        self._discount_rate = discount_rate
        self._learning_rate = learning_rate
        self.epsilon = epsilon
        self._epsilon_decay = epsilon_decay
        self._decay_limit = decay_limit


def main():
    agents = [
        TitForTat,
        Shubik,
        Nydegger,
        Grofman,
        Pavlov,
        TidemanAndChieruzzi,
        Champion,
        Borufsen,
        SecondByGraaskampKatzen
        ]

    grid = {
        "lookback": [1, 2],
        "epsilon": [0.25],
        "epsilon_decay": [0.0],
        "decay_limit": [0.05],
        "learning_rate": [0.1],
        "discount_rate": [0.99 for _ in range(77)],
    }

    results = []
    try:
        space = list(itertools.product(*grid.values()))
        size = len(space)
        best_score = 0
        best_agent = None
        for i, hyperparameters in enumerate(space):
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} | {i + 1}/{size}]",
                *hyperparameters,
                sep="\t",
            )
            result, agent = train_and_evaluate(
                agents, Tabular, epochs=10000, **dict(zip(grid.keys(), hyperparameters))
            )
            results.append(result)
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} | {i + 1}/{size}]",
                f"COOP%={results[-1]['tr_cooperation_percentage']}",
                f"LOSS={results[-1]['tr_final_loss']}",
                f"RANK={results[-1]['tn_rank']}",
                f"SCORE={results[-1]['tn_mean_score']}",
                sep="\t",
            )
            if results[-1]["tn_mean_score"] > best_score:
                best_score = results[-1]["tn_mean_score"]
                best_agent = (results[-1], agent)

    except Exception as e:
        d = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        if results:
            df = pd.DataFrame(results)
            df["agents"] = ",".join([a.__name__ for a in agents])
            df.to_csv(f"results/tabular-{d}.csv")

        if best_agent is not None:
            np.savez_compressed(
                f"models/{d} ({best_score}).npz", q_table=best_agent[1]._q_table
            )
            with open(f"models/{d} ({best_score}).txt", "w") as f:
                f.write(dumps(best_agent[0]))
        print("Quitting evaluation early")


if __name__ == "__main__":
    main()
