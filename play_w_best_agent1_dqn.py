import numpy as np
import pandas as pd
import torch
import torch.nn as nn

from tournament.action import Action
from tournament.agent import Agent
from tournament.agents.q_learning.dqn import DeepQLearner
from tournament.match import Match

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

class ManualAgent(Agent):
    def play_move(self, history, opp_history):
        move = input("Move: ")
        if move == "C":
            return Action.COOPERATE
        elif move == "D":
            return Action.DEFECT
        elif move == "Q":
            raise RuntimeError()


agent = DQN(4, 16, 0.05, 0, 0.1, 0.99)
agent.setup("models/dqn/2022-04-07 01-03-04 - 1hl - 95 - 772.1254838709677 - 11.pt")

manual_agent = ManualAgent()

match = Match(agent, manual_agent)

for i, ((move1, move2), (score1, score2), (reward1, reward2)) in enumerate(
    match.play_moves(continuation_probability=0.99654, limit=1000, noise=0)
):
    print(
        f"{i:<4} | \t {move1:<20} {score1:<8} {f'({reward1})':<20} {move2:<20} {score2:<8} {f'({reward2})':<10}"
    )
