import itertools
from datetime import datetime

import pandas as pd
import torch
import torch.nn as nn

from tournament.agents.q_learning.tabular import TabularQLearner
from tournament.agents.tft import OmegaTFT, TitForTat
from tournament.agents.axelrod_first import (
    Downing,
    Nydegger,
    TidemanAndChieruzzi,
    Grofman
    )
from tournament.agents.axelrod_second import (
    Champion,
    Borufsen,
    SecondByGraaskampKatzen
    )
from tournament.gridsearch import evaluate

class TabularLearner(TabularQLearner):

    def __init__(
        self, lookback: int, epsilon: float, epsilon_decay: float,
        discount_rate: float, learning_rate: float
        ):

        super().__init__()
        self._lookback = lookback
        self._discount_rate = discount_rate
        self._learning_rate = learning_rate
        self._epsilon_decay = epsilon_decay
        self._epsilon = epsilon

def main():
    # no downing : 23.5
    # downing: 25~
    # no downing or borufsen: 25~
    # no tft: 25.3~
    # no tft & tidemanAndChieruzzi: 25.3
    # add grofman no downing: 23.4~
    
    
    agents = [
        TitForTat,
        Nydegger,
        #Downing,
        TidemanAndChieruzzi,
        Champion,
        Borufsen,
        SecondByGraaskampKatzen,
        Grofman
        ]
    grid = {
        "lookback": [1, 2, 4, 6, 8, 10],
        "epsilon": [0.1, 0.2, 0.3],
        "epsilon_decay": [0.0],
        "learning_rate": [0.01, 0.1],
        "discount_rate": [0.99, 0.95, 0.9]
        }

    results = []
    try:
        # unpack all values in grid. take cartesian product (all possible combs)
        # and evaluate.
        for hyperparameters in itertools.product(*grid.values()):
            print(
                f"[{datetime.now().strftime('%y-%m-%d %H-%M-%S')}]",
                *hyperparameters,
                sep="\t"
                )
            results.append(
                evaluate(agents, TabularLearner, **dict(zip(grid.keys(), hyperparameters)))
                )
    except:
        print("Quitting evaluation early.")

    if results:
        df = pd.DataFrame(results)
        df["agents"] = ",".join([a.__name__ for a in agents])
        df.to_csv(f"results/tabular-{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.csv")
            
    
if __name__ == "__main__":
    torch.set_num_threads(12)
    main()
