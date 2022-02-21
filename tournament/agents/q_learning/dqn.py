from random import randint, random
from typing import List, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from tournament.action import Action, random_action
from tournament.agent import TrainableAgent


class QNetwork(nn.Module):
    def __init__(self, lookback):
        super().__init__()

        self.flatten = nn.Flatten()
        self.layer1 = nn.Linear(2 * lookback, lookback)
        self.layer2 = nn.Linear(lookback, lookback)
        self.layer3 = nn.Linear(lookback, 2)

    def forward(self, x):
        x = x.unsqueeze(dim=0)
        x = self.flatten(x)
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        x = torch.relu(self.layer3(x))

        return x


class DeepQLearner(TrainableAgent):
    def __init__(self) -> None:
        self._lookback = 1
        self._discount_rate = 0.99
        self._learning_rate = 1e-3
        self._epsilon = 0.2
        self._epsilon_decay = 0
        self._decay_limit = 0.1

        self._count = 0
        self._batch_size = 8

        self._state = None
        self._q_network = None

    def setup(self) -> None:
        # TODO: implement loading from disk
        self._q_network = QNetwork(self._lookback)
        self._criterion = torch.nn.MSELoss()
        self._optimiser = optim.Adam(
            self._q_network.parameters(), lr=self._learning_rate  # , weight_decay=1e-5
        )
        self._optimiser.zero_grad()

        # randomly initialise the state
        self._state = torch.randint(
            low=0, high=2, size=(self._lookback, 2), dtype=torch.float32
        )

    def teardown(self) -> None:
        # TODO: implement saving to disk
        pass

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        """Plays a move.

        Args:
            history (List[Action]): A chronological history of the agent's past moves.
            opp_history (List[Action]): A chronological history of the opponent's past moves.

        Returns:
            Action: The action to be performed.
        """

        # slowly reduce the exploration rate when above the decay limit
        if self._epsilon > self._decay_limit:
            self._epsilon -= self._epsilon_decay

        # get the Q-values from the model
        self._values = self._q_network(self._state)[0].clone()

        # exploratory moves are picked uniformly at random with probability self._epsilon
        if random() < self._epsilon:
            return random_action()

        # perform the action associated with the highest Q-value for the current state

        # unlike the tabular case, lean towards cooperation if the values are equal
        # (although defection would be fine too), as the model had a tendency to
        # learn Q-values that are both zero to get a random_action() each time
        return Action.COOPERATE if self._values[0] >= self._values[1] else Action.DEFECT

    def update(
        self,
        moves: Tuple[Action, Action],
        scores: Tuple[float, float],
        rewards: Tuple[float, float],
    ) -> None:
        """Updates the internal state of the agent (including its Q-table) following a game iteration.

        Args:
            moves (Tuple[Action, Action]): The actions just performed by the agent and opponent
            scores (Tuple[float, float]): The scores of the agent and opponent
            rewards (Tuple[float, float]): The rewards from the actions just performed
        """

        move = moves[0].value
        state = self._state
        self._state = torch.cat((state[1:], torch.tensor([[move, moves[1].value]])))

        target = (
            rewards[0] + self._discount_rate * self._q_network(self._state)[0].max()
        )

        loss = self._criterion(self._values[move], target)
        loss.backward()

        if self._count % self._batch_size == 0:
            self._optimiser.step()
            self._optimiser.zero_grad()

        self._count += 1


class SingleLookback(DeepQLearner):
    pass


class DoubleLookback(DeepQLearner):
    def __init__(self):
        super().__init__()
        self._lookback = 2
        self._epsilon = 0.25


class TripleLookback(DeepQLearner):
    def __init__(self):
        super().__init__()
        self._lookback = 3
        self._epsilon = 0.2


class LargeLookback(DeepQLearner):
    def __init__(self):
        super().__init__()
        self._lookback = 16
        self._epsilon = 0.1


class HighExplorationRate(DeepQLearner):
    def __init__(self):
        super().__init__()
        self._epsilon = 0.25


class LowExplorationRate(DeepQLearner):
    def __init__(self):
        super().__init__()
        self._epsilon = self._decay_limit


class LowDiscountRate(DeepQLearner):
    def __init__(self):
        super().__init__()
        self._discount_rate = 0.75
