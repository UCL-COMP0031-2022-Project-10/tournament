from random import random
from typing import List, Tuple

import torch
import torch.nn as nn
import torch.optim as optim
from tournament.action import Action, random_action
from tournament.agent import TrainableAgent

torch.manual_seed(42)

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class QNetwork(nn.Module):
    def __init__(self, lookback):
        super().__init__()

        self.flatten = nn.Flatten()
        self.layer1 = nn.Linear(2 * lookback, 32)
        self.layer2 = nn.Linear(32, 32)
        self.layer3 = nn.Linear(32, 2)

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


class DeepQLearner(TrainableAgent):
    def __init__(self) -> None:

        self.lookback = 1
        self.epsilon = 0.2

        self._discount_rate = 0.95
        self._learning_rate = 0.008
        self._epsilon_decay = 0.0  #  0.002
        self._evaluation_epsilon = 0.0
        self._epsilon = self._evaluation_epsilon
        self._decay_limit = 0.05

        self._loss = 0
        self._games = 0  # TODO: remove

        self._count = 0
        self._batch_size = 1

        self._state = None
        self._q_network = QNetwork(self.lookback)

    def get_intial_state(self):
        # randomly initialise the state
        # self._state = torch.randint(
        #     low=0, high=2, size=(self.lookback, 2), dtype=torch.float32
        # )

        # return a nice state
        return torch.zeros(size=(self.lookback, 2), dtype=torch.float32)

    def on_match_start(self):
        self._state = self.get_intial_state()

    def notify_prematch(self):
        self._epsilon = self.epsilon
        self._optimiser.zero_grad()

    def notify_postmatch(self):
        self._games += 1
        self._epsilon = self._evaluation_epsilon

    @property
    def metric(self):
        return self._loss / self._count if self._count > 0 else None

    def setup(self, file=None) -> None:
        if file is not None:
            try:
                self._q_network.load_state_dict(torch.load(file))
            except:
                pass

        self._criterion = torch.nn.HuberLoss()
        self._optimiser = optim.Adam(
            self._q_network.parameters(), lr=self._learning_rate  # , weight_decay=1e-5
        )

    def teardown(self) -> None:
        # torch.save(self._q_network.state_dict(), "model.pt")

        self._epsilon = self._evaluation_epsilon

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        """Plays a move.

        Args:
            history (List[Action]): A chronological history of the agent's past moves.
            opp_history (List[Action]): A chronological history of the opponent's past moves.

        Returns:
            Action: The action to be performed.
        """

        self._prev_state = self._state.clone()
        if history:
            self._state = torch.cat(
                (
                    self._prev_state[1:],
                    torch.tensor([[history[-1].value, opp_history[-1].value]]),
                )
            )

        # slowly reduce the exploration rate when above the decay limit
        if self._epsilon > self._decay_limit:
            self._epsilon -= self._epsilon_decay

        # get the Q-values from the model
        self._values = self._q_network(self._prev_state)

        # exploratory moves are picked uniformly at random with probability self._epsilon
        if random() < self._epsilon:
            return random_action()

        # perform the action associated with the highest Q-value for the current state

        # unlike the tabular case, lean towards cooperation if the values are equal
        # (although defection would be fine too), as the model had a tendency to
        # learn Q-values that are both zero to get a random_action() each time
        return (
            Action.COOPERATE
            if self._values[0, 0] >= self._values[0, 1]
            else Action.DEFECT
        )

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

        prediction = self._values[0, moves[0].value]
        target = (
            rewards[0] + self._discount_rate * self._q_network(self._state)[0].max()
        )

        # print("=>", rewards, prediction.item(), target.item(), self._values)

        loss = self._criterion(prediction, target)
        self._loss += float(loss)
        loss.backward()

        if self._count % self._batch_size == 0:
            self._optimiser.step()
            self._optimiser.zero_grad()

        self._count += 1
