from random import randint, random
from typing import List, Tuple

import numpy as np
from tournament.action import Action, random_action
from tournament.agent import TrainableAgent


class TabularQLearner(TrainableAgent):
    """
    An implementation of a reinforcement learning agent utilising the shallow
    Q-learning algorithm.

    Attributes
    ----------
    _lookback: int
        indicates how many moves back long are the states of the Q-table.
    _discount_rate: float, range is [0,1]
        parameter corresponding to gamma in Q-value update. It indicates how much an agent discounts future rewards, higher value = more
        emphasis on future.
    _learning_rate: float, range is [0,1]
        the step size of the Q-value update. Larger values lead to faster training time but can also cause unstable convergence.
        A value of 0 means the agent does not learn at all.
    _epsilon: float, range is [0,1]
        The exploration parameter for this agent. It is the probability of an agent exploring its environment, i.e., executing a random action instead of
        the best one and observing its payoff.
    _epsilon_decay: float, range is [0, self._epsilon)
        How much the exploration parameter decays after every move. Exploration is encouraged at the start of training, but it is not as valuable later on
        so we slowly decrease it to _decay_limit.
    _decay_limit: float, range is [0, self._epsilon]
        The lowest value for self._epsilon. Once it has decayed to this value, it stops decreasing.
    _q_table: dict[tuple[tuple[Action, Action]], list[float]], length of state = _lookback
        Contains a tuple of states and a list containing the corresponding Q-values. the first value in the list is the Q-value for cooperating and the second value
        is the Q-value for defecting. The agent looks up the Q-values for current state and executes the move that gives highest Q-value.
    _state: tuple[tuple[Action, Action]], length of state = _lookback
        Used to store the current state for update method.
    """

    def __init__(self) -> None:
        self.epsilon = 0.2
        self._lookback = 1
        self._discount_rate = 0.99
        self._learning_rate = 0.001
        self._evaluation_epsilon = 0.0
        self._epsilon_decay = 0
        self._decay_limit = 0.1

        self._q_table = None
        self._state = None
        self._epsilon = self._evaluation_epsilon

    def get_initial_state(self):
        """Returns a cooperative initial state."""

        return tuple(0 for _ in range(self._lookback))

    def setup(self) -> None:
        self._q_table = np.zeros(shape=tuple(4 for _ in range(self._lookback)) + (2,))

    def on_match_start(self):
        # initialise the state
        self._state = self.get_initial_state()

    def load(self, filename):
        self._q_table = np.load(filename)["q_table"]

    def teardown(self) -> None:
        self._epsilon = self._evaluation_epsilon

    def notify_prematch(self):
        self._epsilon = self.epsilon

    def notify_postmatch(self):
        self._epsilon = self._evaluation_epsilon

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        """Plays a move.

        Args:
            history (List[Action]): A chronological history of the agent's past moves.
            opp_history (List[Action]): A chronological history of the opponent's past moves.

        Returns:
            Action: The action to be performed.
        """

        self._prev_state = self._state
        if history:
            self._state = self._prev_state[1:] + (
                2 * history[-1].value + opp_history[-1].value,
            )

        # slowly reduce the exploration rate when above the decay limit
        if self._epsilon > self._decay_limit:
            self._epsilon -= self._epsilon_decay

        # exploratory moves are picked uniformly at random with probability self._epsilon
        if random() < self._epsilon:
            return random_action()

        # print("PREV STATE:", self._prev_state)
        # print("NEW STATE:", self._state)
        # print("Q-values:", self._q_table[self._prev_state])

        # perform the action associated with the highest Q-value for the current state
        if self._q_table[self._prev_state][0] >= self._q_table[self._prev_state][1]:
            return Action.COOPERATE

        return Action.DEFECT

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

        self._q_table[self._prev_state][move] += self._learning_rate * (
            rewards[0]
            + self._discount_rate * self._q_table[self._state].max()
            - self._q_table[self._prev_state][move]
        )


# class SingleLookback(TabularQLearner):
#     pass


# class DoubleLookback(TabularQLearner):
#     epsilon = 0.25

#     def __init__(self):
#         super().__init__()
#         self._lookback = 2


# class TripleLookback(TabularQLearner):
#     epsilon = 0.2

#     def __init__(self):
#         super().__init__()
#         self._lookback = 3


# class HighExplorationRate(TabularQLearner):
#     epsilon = 0.25


# class LowExplorationRate(TabularQLearner):
#     def __init__(self):
#         super().__init__()
#         self.epsilon = self._decay_limit


# class LowDiscountRate(TabularQLearner):
#     def __init__(self):
#         super().__init__()
#         self._discount_rate = 0.75


class NiceTabularQLearner(TabularQLearner):
    def get_initial_state(self):
        return tuple(0 for _ in range(self._lookback))


class NonNiceTabularQLearner(TabularQLearner):
    def get_initial_state(self):
        return tuple(randint(0, 3) for _ in range(self._lookback))
