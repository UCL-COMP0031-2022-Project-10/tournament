from random import randint, random
from typing import List, Tuple

import numpy as np
from tournament.action import Action, random_action
from tournament.agent import TrainableAgent


class TabluarQLearner(TrainableAgent):
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

    _lookback = 1
    _discount_rate = 0.99
    _learning_rate = 0.001
    _epsilon = 0.2
    _epsilon_decay = 0
    _decay_limit = 0.1

    def __init__(self):
        self._q_table = None
        self._state = None

    def setup(self) -> None:
        # TODO: implement loading from disk
        self._q_table = np.zeros(shape=tuple(4 for _ in range(self._lookback)) + (2,))

        # randomly initialise the state
        self._state = tuple(randint(0, 3) for _ in range(self._lookback))

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

        # exploratory moves are picked uniformly at random with probability self._epsilon
        if random() < self._epsilon:
            return random_action()

        # perform the action associated with the highest Q-value for the current state
        if self._q_table[self._state][0] > self._q_table[self._state][1]:
            return Action.COOPERATE
        elif self._q_table[self._state][0] < self._q_table[self._state][1]:
            return Action.DEFECT

        return random_action()

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
        self._state = state[1:] + (2 * move + moves[1].value,)

        self._q_table[state][move] += self._learning_rate * (
            rewards[0]
            + self._discount_rate * self._q_table[self._state].max()
            - self._q_table[state][move]
        )


class SingleLookback(TabluarQLearner):
    pass


class DoubleLookback(TabluarQLearner):
    def __init__(self):
        super().__init__()
        self._lookback = 2
        self._epsilon = 0.25


class TripleLookback(TabluarQLearner):
    def __init__(self):
        super().__init__()
        self._lookback = 3
        self._epsilon = 0.2


class HighExplorationRate(TabluarQLearner):
    def __init__(self):
        super().__init__()
        self._epsilon = 0.25


class LowExplorationRate(TabluarQLearner):
    def __init__(self):
        super().__init__()
        self._epsilon = self._decay_limit


class LowDiscountRate(TabluarQLearner):
    def __init__(self):
        super().__init__()
        self._discount_rate = 0.75
