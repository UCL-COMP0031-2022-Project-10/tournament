import itertools
from datetime import datetime

import pandas as pd
import torch
import torch.nn as nn

from tournament.agents.constant import AllC, AllD
from tournament.agents.q_learning.dqn import DeepQLearner
from tournament.agents.tft import OmegaTFT, TitForTat
from tournament.gridsearch import evaluate, train_and_evaluate


class QNetwork(nn.Module):
    def __init__(self, lookback, n1=32):
        super().__init__()

        self.flatten = nn.Flatten()
        self.layer1 = nn.Linear(2 * lookback, n1)
        self.layer2 = nn.Linear(n1, n1)
        self.layer3 = nn.Linear(n1, 2)

        nn.init.kaiming_uniform_(self.layer1.weight, mode="fan_in", nonlinearity="relu")
        nn.init.kaiming_uniform_(self.layer2.weight, mode="fan_in", nonlinearity="relu")
        nn.init.kaiming_uniform_(self.layer3.weight, mode="fan_in", nonlinearity="relu")

    def forward(self, x):
        x = x.unsqueeze(dim=0)
        x = self.flatten(x)
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        x = torch.relu(self.layer3(x))

        return x


class DQN(DeepQLearner):
    def __init__(
        self, lookback, n1, epsilon, epsilon_decay, learning_rate, discount_rate
    ):
        super().__init__()

        self.lookback = lookback
        self.epsilon = epsilon
        self._epsilon_decay = epsilon_decay
        self._learning_rate = learning_rate
        self._discount_rate = discount_rate
        self._q_network = QNetwork(self.lookback, n1)


def main():
    agents = [TitForTat, OmegaTFT, AllC, AllD]

    grid = {
        "lookback": [2, 4, 8, 10],
        "n1": [8, 12, 16, 32, 48, 64],
        "epsilon": [0.1, 0.2],
        "epsilon_decay": [0.0],
        "learning_rate": [0.001],
        "discount_rate": [0.95, 0.99],
    }

    grid = {
        "lookback": [8],
        "n1": [8, 12, 16, 20],
        "epsilon": [0.2],
        "epsilon_decay": [0.0],
        "learning_rate": [0.001],
        "discount_rate": [0.95],
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
                agents, DQN, **dict(zip(grid.keys(), hyperparameters))
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
                best_agent = (results[-1]["model"], agent)

    except:
        print("Quitting evaluation early")

    d = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    if results:
        df = pd.DataFrame(results)
        df["agents"] = ",".join([a.__name__ for a in agents])
        df.to_csv(f"results/dqn-1hl-{d}.csv")

    if best_agent is not None:
        torch.save(
            best_agent[1]._q_network.state_dict(), f"models/{d} ({best_score}).pt"
        )
        with open(f"models/{d} ({best_score}).txt", "w") as f:
            f.write(best_agent[0])


if __name__ == "__main__":
    main()
