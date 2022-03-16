import itertools
from datetime import datetime

import pandas as pd
import torch
import torch.nn as nn

from tournament.agents.q_learning.rnn import RNNQLearner
from tournament.agents.tft import OmegaTFT, TitForTat
from tournament.agents.axelrod_first import (
    Downing,
    Nydegger,
    TidemanAndChieruzzi
    )
from tournament.agents.axelrod_second import (
    Champion,
    Borufsen,
    SecondByGraaskampKatzen
    )
from tournament.gridsearch import evaluate

class RNN(nn.Module):
    def __init__(
        self, lookback: int, hidden_size: int=4, num_layers: int=1
        ):
        
        super().__init__()

        self._flatten = nn.Flatten()
        self._num_layers = num_layers
        self._hidden_size = hidden_size
        self._input_size = 2 * lookback
        self._rnn = nn.RNN(input_size=self._input_size, hidden_size=self._hidden_size,
                           num_layers=self._num_layers, batch_first=True)
        self._fc = nn.Linear(self._hidden_size, 2)

    def forward(self, x) -> tuple:

        x = x.unsqueeze(dim=0)
        x = self._flatten(x)
        x = x[None, :] # add extra dimension to [1,1,6]
        hidden = self._init_hidden()
        out, hidden = self._rnn(x, hidden)
        out = out.reshape(-1, self._hidden_size)
        out = self._fc(out)
        return out, hidden

    def _init_hidden(self):

        return torch.zeros(self._num_layers, 1, self._hidden_size)


class RNNLearner(RNNQLearner):
    def __init__(
        self, lookback: int, hidden_size: int, num_layers: int, epsilon: float,
        epsilon_decay: float, discount_rate: float, learning_rate: float):

        super().__init__()
        self.lookback = lookback
        self.epsilon = epsilon
        self._epsilon_decay = epsilon_decay
        self._discount_rate = discount_rate
        self._learning_rate = learning_rate
        self._q_network = RNN(self.lookback, hidden_size, num_layers)

def main():
    agents = [
        TitForTat,
        Nydegger,
        Downing,
        TidemanAndChieruzzi,
        Champion,
        Borufsen,
        SecondByGraaskampKatzen
        ]
    grid = {
        "lookback": [1, 2, 4, 6, 8],
        "hidden_size": [1, 4, 32, 64],
        "num_layers": [1],
        "epsilon": [0.1],
        "epsilon_decay": [0.0],
        "learning_rate": [0.01],
        "discount_rate": [0.99]
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
                evaluate(agents, RNNLearner, **dict(zip(grid.keys(), hyperparameters)))
                )
    except:
        print("Quitting evaluation early.")

    if results:
        df = pd.DataFrame(results)
        df["agents"] = ",".join([a.__name__ for a in agents])
        df.to_csv(f"results/rnn-{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.csv")
            
    
if __name__ == "__main__":
    torch.set_num_threads(12)
    main()
