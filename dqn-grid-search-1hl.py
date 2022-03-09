import itertools
from datetime import datetime

import numpy as np
import pandas as pd
import torch
import torch.nn as nn

from tournament.action import Action
from tournament.agents.agents import AGENTS
from tournament.agents.q_learning.dqn import DeepQLearner
from tournament.agents.tft import OmegaTFT, TitForTat
from tournament.environments.multiple import MultipleRuleBasedAgentEnvironment
from tournament.tournament import RoundRobinTournament


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


def evaluate(
    agents, lookback, n1, epsilon, epsilon_decay, learning_rate, discount_rate
):
    env = MultipleRuleBasedAgentEnvironment(agents, silent=True)
    agent = DQN(lookback, n1, epsilon, epsilon_decay, learning_rate, discount_rate)
    env.train(
        trainee=agent,
        limit=200,
        epochs=200,
    )

    s = sum(env.counts.values())

    agent._q_network.eval()

    tournament = RoundRobinTournament(AGENTS, [agent])
    scores, times = tournament.play(
        continuation_probability=0.99654, repetitions=50, jobs=12
    )
    results = {agent: sum(scores[agent]) / len(scores[agent]) for agent in scores}

    return {
        "model": str(agent._q_network),
        "tr_cooperation_percentage": env.counts[Action.COOPERATE] / s,
        "tr_defection_percentage": env.counts[Action.DEFECT] / s,
        "tr_final_loss": env.metric_history[-1],
        "tr_mean_reward": np.mean(env.rewards),
        "tr_cumul_reward": np.sum(env.rewards),
        "tr_cumul_regret": np.sum(3 - np.array(env.rewards)),
        "tn_rank": sorted(results, key=results.get, reverse=True).index(DQN) + 1,
        "tn_mean_score": results[DQN],
        "tn_mean_time": sum(times[DQN]),
    }


def main():
    agents = [
        TitForTat,
        OmegaTFT,
    ]

    grid = {
        "lookback": [1, 2, 4, 6, 8, 10],
        "n1": [4, 8, 12, 16, 24, 32, 64, 96, 128],
        "epsilon": [0.05, 0.1, 0.2],
        "epsilon_decay": [0.0],
        "learning_rate": [0.01, 0.001],
        "discount_rate": [0.95, 0.99],
    }

    results = []

    try:
        for hyperparameters in itertools.product(*grid.values()):
            print(*hyperparameters)
            results.append(evaluate(agents, **dict(zip(grid.keys(), hyperparameters))))
    except:
        print("Quitting evaluation early.")

    if results:
        df = pd.DataFrame(results)
        df["agents"] = ",".join([a.__name__ for a in agents])
        df.to_csv(f"results/dqn-1hl-{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.csv")


if __name__ == "__main__":
    main()
