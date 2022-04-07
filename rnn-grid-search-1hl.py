import itertools
from datetime import datetime

import pandas as pd
import torch
import torch.nn as nn

from tournament.agents.q_learning.rnn import RNNQLearner
from tournament.agents.tft import OmegaTFT, TitForTat
from tournament.agents.axelrod_first import (
    Davis,
    Downing,
    Feld,
    Grofman,
    Grudger,
    Joss,
    Nydegger,
    Shubik,
    SteinAndRapoport,
    TidemanAndChieruzzi,
    Tullock,
)
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
from tournament.gridsearch import train_and_evaluate

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
    agents = agents = [
        TitForTat,
        TidemanAndChieruzzi,
        Borufsen,
        SecondByGraaskampKatzen,
        Nydegger,
        Grofman,
        Shubik,
        Champion,
        Leyvraz
        ] 

    grid = {
        "lookback": [1, 2, 4, 8],
        "hidden_size": [8,12,16,24],
        "epsilon": [0.05, 0.1, 0.2],
        "num_layers" : [1],
        "epsilon_decay": [0.0],
        "learning_rate": [0.001, 0.01, 0.05, 0.1],
        "discount_rate": [0.95, 0.99],
    }

    d = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
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
            result, agent = train_and_evaluate(
                agents, RNNLearner, epochs=250, **dict(zip(grid.keys(), hyperparameters))
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
            if result["tn_mean_score"] > 750 or result["tn_rank"] > 27:
                torch.save(
                    agent._q_network.state_dict(),
                    f"models/dqn/{d} - 1hl - {i} - {result['tn_mean_score']} - {result['tn_rank']}.pt",
                )
                with open(
                    f"models/dqn/{d} - 1hl - {i} - {result['tn_mean_score']} - {result['tn_rank']}.txt",
                    "w",
                ) as f:
                    f.write(dumps(result))
    except Exception as e:
        print("Qutting evaluation early:", str(e))
    except:
        print("Quitting evaluation early")

    if results:
        df = pd.DataFrame(results)
        df["agents"] = ",".join([a.__name__ for a in agents])
        df.to_csv(f"results/dqn/dqn-1hl-{d}.csv")


if __name__ == "__main__":
    main()
