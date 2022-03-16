from random import random
from typing import List, Tuple

import torch
import torch.nn as nn
import torch.optim as optim
from tournament.action import Action, random_action
from tournament.agent import TrainableAgent

torch.manual_seed(42)

class RNN(nn.Module):
    def __init__(self, lookback):
        super().__init__()
        self._flatten = nn.Flatten()
        self._num_layers = 1
        self._input_size = 2 * lookback
        self._hidden_sz = 32         # hyperparameter we can tune.
        self._rnn = nn.RNN(input_size=self._input_size, hidden_size=self._hidden_sz, num_layers=self._num_layers, batch_first=True)
        self._fc = nn.Linear(self._hidden_sz, 2)

    def forward(self, x):
        x = x.unsqueeze(dim=0)
        x = self._flatten(x)
        x = x[None, :]
        hidden = self.init_hidden()
        out, hidden = self._rnn(x, hidden)
        out = out.reshape(-1, self._hidden_sz)
        out = self._fc(out)
        return out, hidden

    def init_hidden(self):
        return torch.zeros(self._num_layers, 1, self._hidden_sz)

class RNNQLearner(TrainableAgent):
    lookback = 3
    epsilon = 0.2
    decay_limit = 0.05

    def __init__(self) -> None:
        self._discount_rate = 0.95
        self._learning_rate = 0.008
        self._epsilon_decay = 0.0  #  0.002

        self._loss = 0
        self._games = 0  # TODO: remove

        self._count = 0
        self._batch_size = 1

        self._state = None
        self._q_network = RNN(self.lookback)

    def on_match_start(self):
        # randomly initialise the state
        self._state = torch.randint(
            low=0, high=2, size=(self.lookback, 2), dtype=torch.float32
        )

    def notify_prematch(self):
        self._epsilon = self.epsilon
        self._decay_limit = self.decay_limit
        self._optimiser.zero_grad()

    def notify_postmatch(self):
        self._games += 1
        # print(
        #     f"POSTMATCH {self._games}:",
        #     self._values,
        # )

    @property
    def metric(self):
        return self._loss / self._count if self._count > 0 else None

    def setup(self) -> None:
        try:
            self._q_network.load_state_dict(torch.load("rnnmodel.pt"))
        except:
            pass

        self._criterion = torch.nn.MSELoss()
        self._optimiser = optim.Adam(
            self._q_network.parameters(), lr=self._learning_rate  # , weight_decay=1e-5
        )

    def teardown(self) -> None:
        # torch.save(self._q_network.state_dict(), "rnnmodel.pt")
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
        self._values, hidden = self._q_network(self._state)

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

        move = moves[0].value
        state = self._state
        self._state = torch.cat((state[1:], torch.tensor([[move, moves[1].value]])))
        
        prediction = self._values[0, move]
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
