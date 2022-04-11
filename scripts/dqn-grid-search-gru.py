import itertools
from datetime import datetime

import pandas as pd
import torch
import torch.nn as nn

from tournament.agents.axelrod_first import Downing, Nydegger, TidemanAndChieruzzi
from tournament.agents.axelrod_second import Borufsen, Champion, GraaskampAndKatzen
from tournament.agents.constant import AllC, AllD
from tournament.agents.q_learning.dqn import DeepQLearner
from tournament.agents.tft import OmegaTFT, TitForTat
from tournament.gridsearch import evaluate, train_and_evaluate


class QNetwork(nn.Module):
    def __init__(self, lookback):
        super().__init__()

        self.flatten = nn.Flatten()
        self.gru = nn.GRU(2, 2, 2, batch_first=True)
        self.layer4 = nn.Linear(2 * lookback, 2)

        nn.init.kaiming_uniform_(self.layer4.weight, mode="fan_in", nonlinearity="relu")

    def forward(self, x):
        x = x.unsqueeze(dim=0)
        x, hn = self.gru(x)
        x = self.flatten(x)
        x = torch.relu(self.layer4(x))

        return x


class DQN(DeepQLearner):
    def __init__(self, lookback, epsilon, epsilon_decay, learning_rate, discount_rate):
        super().__init__()

        self.lookback = lookback
        self.epsilon = epsilon
        self._epsilon_decay = epsilon_decay
        self._learning_rate = learning_rate
        self._discount_rate = discount_rate
        self._q_network = QNetwork(self.lookback)


def main():
    epochs = 250

    agents = [
        TitForTat,
        Nydegger,
        TidemanAndChieruzzi,
        Champion,
        Borufsen,
        GraaskampAndKatzen,
    ]

    grid = {
        "lookback": [4, 8],
        "epsilon": [0.2],
        "epsilon_decay": [0.0],
        "learning_rate": [0.001, 0.01],
        "discount_rate": [0.95, 0.99],
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
                agents, DQN, epochs, **dict(zip(grid.keys(), hyperparameters))
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
        df.to_csv(f"results/dqn-gru-{d}.csv")

    if best_agent is not None:
        torch.save(
            best_agent[1]._q_network.state_dict(), f"models/{d} ({best_score}).pt"
        )
        with open(f"models/{d} ({best_score}).txt", "w") as f:
            f.write(best_agent[0])


if __name__ == "__main__":
    main()
