import json
import os.path
from random import choice, random
from typing import List, Tuple

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

    OUTCOMES = {
        0: (Action.COOPERATE, Action.COOPERATE),
        1: (Action.COOPERATE, Action.DEFECT),
        2: (Action.DEFECT, Action.COOPERATE),
        3: (Action.DEFECT, Action.DEFECT),
    }

    def __init__(self):
        self._lookback = 1
        self._discount_rate = 0.99
        self._learning_rate = 0.001
        self._epsilon = 0.1
        self._epsilon_decay = 0
        self._decay_limit = 0.1

        self._q_table = None
        self._current_state = None
        self._state = ()

    def setup(self) -> None:

        """
        If a file called "tabluar_q_learner_table.json" exists then we load in the trained Q-values; otherwise, we need to build
        the state space according to the length of history available to self and initialise all of it's values to 0.
        """

        if os.path.exists("tabluar_q_learner_table.json"):
            with open("tabluar_q_learner_table.json", "r") as fp:
                self._q_table = json.loads(fp)
        else:
            self._q_table = self._build_q_table()

    def teardown(self) -> None:

        """
        Saves self._q_table to a file called "tabluar_q_learner_table.json". This file contains the final Q-values after training
        and is loaded in when the agents compete in the tournament.
        """

        pass

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:

        """
        Use this method to decide whether to cooperate or defect against adversary. Firstly, we decay the
        exploration parameter and explore with probability self._epsilon. Exploring means to execute a random action
        and observing its payoff. Next, construct the current state by utilising the histories and look-up the Q-value
        for the associated state. Execute the action with the higher Q-value; if they are equal, do a random one.

        Parameters
        ----------
        history: Contains all of the moves made by self against the adversary so far in the current match.
        opp_history: Contains all of the moves made by the adversary against self so far in the current match.

        Returns
        -------
        Action.COOPERATE or Action.DEFECT indicating what action self should perform.
        """

        # slowly reduce the exploration rate when above the decay limit
        if self._epsilon > self._decay_limit:
            self._epsilon -= self._epsilon_decay

        # initial or exploratory moves are picked uniformly at random
        if len(history) < self._lookback or random() < self._epsilon:
            return random_action()

        self._state = self._construct_current_state(history, opp_history)

        # execute action that has highest q_val for associated state.
        q_vals = self._q_table[self._state]
        if q_vals[0] > q_vals[1]:
            # q_val for coop > q_val for defect
            return Action.COOPERATE
        elif q_vals[0] < q_vals[1]:
            return Action.DEFECT

        # they are equal so random.
        return random_action()

    def update(
        self,
        moves: Tuple[Action, Action],
        scores: Tuple[float, float],
        rewards: Tuple[float, float],
    ) -> None:

        """
        Training environment calls this method after a play move as been called to update the existing Q-values for
        the state when the move was played.

        Parameters
        ----------
        moves: A tuple containing the actions executed by each agent after play_move was called. Only has most recent move.
        scores
        scores: Cumulative score of each agent so far in the tournament. It is the sum of the rewards from each each match. Not used in this method.
        rewards: Corresponds to payoff matrix values for the outcome specified by moves. The first element is the reward for self while
                    the second reward is the reward for opponent.
        """
        if not self._state:
            return

        # remove oldest move and append most recent move
        new_state = self._state[1:] + (moves,)

        # index the list for key. index 0 = Q-value for cooperating, 1 = defecting
        idx = moves[0].value
        self._q_table[self._state][idx] += self._learning_rate * (
            rewards[0]
            + self._discount_rate * max(self._q_table[new_state])
            - self._q_table[self._state][idx]
        )

    """
        State is returned in a oldest to newest ordering.
    """

    def _construct_current_state(
        self, history: List[Action], opp_history: List[Action]
    ) -> tuple[tuple[Action, Action]]:
        """Constructs the current state from the agent's history and the opponent's history.

        Args:
            history (List[Action]): The agent's history.
            opp_history (List[Action]): The opponent's history.

        Returns:
            tuple[tuple[Action, Action]]: The current state.
        """

        return tuple(zip(history[-self._lookback :], opp_history[-self._lookback :]))

    def _build_q_table(self) -> dict[tuple[tuple[Action, Action]], List[float]]:

        """
        If there isn't a file containing saved Q-values, we need to construct the Q table ourselves. It is simply done by creating every possible
        state for _lookback and initialising its Q-values for cooperating and defecting to 0.

        A Q-table holds the q values for environment states and actions. The table is
        iteratively modified as the agent updates its q values. An example of q table is given
        below for history size 1.

        State = (Previous action of Q-learning agent, Previous action of opponent)
        The q-values in the table below are what you would expect for a TFT agent.

        The first element in the list for each key is the q-value for cooperating given the state,
        meanwhile the second element is the q-value for defecting given the state.

        Example of Q-Table for TFT agent with history of 1 move.
           State    |    Cooperate   |   Defect
          --------------------------------------
          ((C, C))  |        1       |   0
          ((C, D))  |        0       |   1
          ((D, C))  |        1       |   0
          ((D, D))  |        0       |   1

        The space complexity: O(4^h) where h = size of history. Each increment of history adds 4 branches to each branch of state-tree.

        This function constructs a q-table with all values initialised to zero to begin with. Essentially,
        the first move is random.
        """

        q_table = {}
        # base_4 vector of length 4^history. The ith value represents the outcome of the previous ith game in history.
        vec = [0] * self._lookback
        while vec != [-1]:
            """
            State space is constructed as follows:
            Initialise a base 4 vector with length len_history. The ith value in the vector represents the outcome of the ith previous game.
            0 = (C, C), 1 = (C, D), 2 = (D, C), 3 = (D, D)
            As you increment the vector from 0 - (4^(h) - 1), each possible sequence of outcomes is constructed
            E.g., the vector 3212 represents the sequence ((D, D), (D, C), (C, D), (D, C))
            """
            q_table[self._create_key(vec)] = [0.0, 0.0]
            vec = self._increment_vec(vec)

        return q_table

    def _create_key(self, vec: List[int]) -> tuple[tuple[Action, Action]]:
        """Takes a base_4 number and constructs the corresponding state.

        The number of digits in the number = self._lookback.

        Args:
            vec (List[int]): a base_4 number in a list, in which the value at index 0
                             is the most significant quaternary digit. A list is used
                             for ease of incrementation. Each quaternary digit corresponds
                             to an outcome. The combination of digits therein corresponds
                             to a state.

        Returns:
            tuple[tuple[Action, Action]]: A possible state of length self._lookback
        """

        return tuple(self.OUTCOMES[elem] for elem in vec)

    def _increment_vec(self, vec: List[int]) -> List[int]:

        """
        Used to increment a base_4 number. Once you have reached the maximum value ((4 ^ len(vec)) - 1), we set vec == [-1] indicating an overflow, so that the
        loop in _build_q_table is broken. Each digit corresponds to an outcome, and the combination of the digits corresponds to a state.

        Parameters
        ----------
        vec:
            base_4 number in list format. Using a list due to the simplicity of incrementing it.

        Returns
        -------
        the base 4 number represented by vec + 1 or [-1] if we have incremented past the max value representable by vec.
        """

        curr = -1
        while 1:
            if curr == -1 * (len(vec) + 1):
                # overflow, which means we have generated all possible states. Time to break loop.
                return [-1]
            if vec[curr] + 1 == 4:
                vec[curr] = 0
                curr -= 1
            else:
                vec[curr] += 1
                break

        return vec
