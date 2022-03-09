import itertools
from datetime import datetime

import pandas as pd
import torch
import torch.nn as nn

from tournament.agents.q_learning.dqn import DeepQLearner
from tournament.agents.tft import OmegaTFT, TitForTat
from tournament.gridsearch import evaluate


class QNetwork(nn.Module):
    def __init__(self, lookback, n1=32, n2=32):
        super().__init__()

        self.flatten = nn.Flatten()
        self.layer1 = nn.Linear(2 * lookback, n1)
        self.layer2 = nn.Linear(n1, n2)
        self.layer3 = nn.Linear(n2, n1)
        self.layer4 = nn.Linear(n1, 2)

        nn.init.kaiming_uniform_(self.layer1.weight, mode="fan_in", nonlinearity="relu")
        nn.init.kaiming_uniform_(self.layer2.weight, mode="fan_in", nonlinearity="relu")
        nn.init.kaiming_uniform_(self.layer3.weight, mode="fan_in", nonlinearity="relu")
        nn.init.kaiming_uniform_(self.layer4.weight, mode="fan_in", nonlinearity="relu")

    def forward(self, x):
        x = x.unsqueeze(dim=0)
        x = self.flatten(x)
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        x = torch.relu(self.layer3(x))
        x = torch.relu(self.layer4(x))

        return x


class DQN(DeepQLearner):
    def __init__(
        self, lookback, n1, n2, epsilon, epsilon_decay, learning_rate, discount_rate
    ):
        super().__init__()

        self.lookback = lookback
        self.epsilon = epsilon
        self._epsilon_decay = epsilon_decay
        self._learning_rate = learning_rate
        self._discount_rate = discount_rate
        self._q_network = QNetwork(self.lookback, n1, n2)


def main():
    agents = [
        TitForTat,
        OmegaTFT,
    ]

    grid = {
        "lookback": [4, 8],
        "n1": [4, 8, 12, 16, 24, 32],
        "n2": [4, 8, 12, 16, 24, 32],
        "epsilon": [0.2],
        "epsilon_decay": [0.0],
        "learning_rate": [0.01, 0.001],
        "discount_rate": [0.95],
    }

    results = []
    try:
        for hyperparameters in itertools.product(*grid.values()):
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}]",
                *hyperparameters,
                sep="\t",
            )
            results.append(
                evaluate(agents, DQN, **dict(zip(grid.keys(), hyperparameters)))
            )
    except:
        print("Quitting evaluation early.")

    if results:
        df = pd.DataFrame(results)
        df["agents"] = ",".join([a.__name__ for a in agents])
        df.to_csv(f"results/dqn-2hl-{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.csv")


if __name__ == "__main__":
    main()
