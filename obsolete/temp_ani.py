import itertools
from datetime import datetime

import pandas as pd
import torch
import torch.nn as nn

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
    Shubik,
)
from tournament.agents.random import RandomAgent
from tournament.agents.pavlov import Pavlov
from tournament.agents.axelrod_second import (
    Borufsen,
    Champion,
    Leyvraz,
    SecondByBlackK83R,
    GraaskampAndKatzen,
    Harrington,
    TidemanAndChieruzzi2,
    Weiner,
    White,
)
from tournament.agents.constant import AllC, AllD
from tournament.gridsearch import evaluate


class TabularLearner(TabularQLearner):
    def __init__(
        self,
        lookback: int,
        epsilon: float,
        epsilon_decay: float,
        discount_rate: float,
        learning_rate: float,
    ):

        super().__init__()
        self._lookback = lookback
        self._discount_rate = discount_rate
        self._learning_rate = learning_rate
        self._epsilon_decay = epsilon_decay
        self._epsilon = epsilon


def main():
    # Set: TFT, Nydegger, Downing, TNC, Champion, SGK, Borufsen = 25

    # TFT, Nydegger, TNC, Champion, SGK, borufsen : 23.5
    # TFT, Nydegger, TNC, Downing, Champion, SGK : 25
    # Nydegger, Downing, TNC, Champion, SGK, Borufsen = 25.3
    # Nydegger, Downing, Champion, SGK, Borufsen = 25.3
    # TFT, Nydegger, TNC, Champion, SGK, Borufsen, Grofman = 23.4
    # TFT, TNC, Champion, Borufsen, SGK, Grofman, eps=0.01,lr=0.01, =

    """
    New testing:
    Standard set:
    epsilon = 0.01, lr = 0.1, lb = 1

    r1: Agents = {TFT, NYD, DOW, TNC, CHA, BOR, SGK, GRO} Avg rank = 23.7
    r2: same agents change lr to 0.2. Avg Rank = 24.1
    r3: {TFT, NYD, TNC, CHA, BOR, SGK, GRO}. Avg Rank = 23
    r4: {TFT, NYD, TNC, BOR, SGK, GRO}. Avg rnk = 23.4
    r5: {TFT, NYD, TNC, CHA, BOR, SGK, GRO, SHUBIK}. Avg rnk = 25.8
    r6: {TFT, NYD, CHA, BOR, SGK, GRO}. Avg rank = 23.5
    r7: {TFT, TNC, CHA, BOR, SGK, GRO}. Avg rank = 22.7
    r8: {TFT, TNC, CHA, BOR, GRO}. Avg rank = 23.6
    r9: add leyvraz
    """

    agents = [
        # AllC,
        # AllD,
        TitForTat,
        # RandomAgent,
        # Davis,
        Shubik,
        # SteinAndRapoport,
        # Grudger,
        Nydegger,
        Grofman,
        # Downing,
        # Feld,
        # Joss,
        Pavlov,
        # OmegaTFT,
        # TFTT,
        # TTFT,
        # GradualTFT,
        # GenerousTFT,
        TidemanAndChieruzzi,
        Champion,
        Borufsen,
        # Leyvraz,
        # Harrington,
        # White,
        # SecondByBlackK83R,
        # TidemanAndChieruzzi2,
        GraaskampAndKatzen,
        # Weiner,
        # Tullock,
    ]
    grid = {
        "lookback": [1],
        "epsilon": [0.01],
        "epsilon_decay": [0],
        "learning_rate": [0.1],
        "discount_rate": [0.99 for _ in range(150)],
    }

    results = []
    try:
        # unpack all values in grid. take cartesian product (all possible combs)
        # and evaluate.
        for hyperparameters in itertools.product(*grid.values()):
            print(
                f"[{datetime.now().strftime('%y-%m-%d %H-%M-%S')}]",
                *hyperparameters,
                sep="\t",
            )
            results.append(
                evaluate(
                    agents, TabularLearner, **dict(zip(grid.keys(), hyperparameters))
                )
            )
    except:
        print("Quitting evaluation early.")

    if results:
        df = pd.DataFrame(results)
        df["agents"] = ",".join([a.__name__ for a in agents])
        df.to_csv(
            f"results/bestpool-tabular-{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.csv"
        )


if __name__ == "__main__":
    torch.set_num_threads(12)
    main()
