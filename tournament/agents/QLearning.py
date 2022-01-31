from typing import List  
from tournament.action import Action
from tournament.agent import Agent 
from match import PAYOFF_MATRIX
from random import random

class QLearning(Agent):
    '''
        An implementation of a reinforcement learning agent utilising the shallow
        Q-learning algorithm.
    '''
    def __init__(self):

        self._len_history = 1 # give access to 1 move back.
        self._discount_rate = 0.99
        self._learning_rate = 0.001
        self._epsilon = 0.05
        self._epsilon_decay = 0.00001
        self._decay_limit = 0.1
        self._q_table = self._build_q_table(self._len_history)
        self._prev_state = None       # used to hold the state before an agent performs a move. This is then used in updating the q-values with state before move.

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:

        '''
            1) If there is history => update q values from previous move.
            2) reduce exploration rate slowly to a minimum of self._decay_limit.
            3) Perform random action with prob self._epsilon.
            4) Find the action that gives you highest q value for current state and execute it. If they are equal, do random.
        '''

        if history:
            # update the q values from previous move before executing current move. Could move this to tournament so that it is called after a move is executed
            # rather than before.
            self._update_q_values(history, opp_history)

        if self._epsilon > self._decay_limit:
            # slowly reduce exploration rate.
            self._epsilon -= self._epsilon_decay

        if random() < self._epsilon:
            # explore, so we do random move.
            return Action.COOPERATE if random() < 0.5 else Action.DEFECT

        curr_state = self._construct_current_state(history, opp_history)
        self._prev_state = curr_state    # save state before executing move, so we can update the q value next turn.

        # execute action that has highest q_val for associated state.
        q_vals = self._q_table[curr_state]
        if q_vals[0] > q_vals[1]:
            # q_val for coop > q_val for defect.
            return Action.COOPERATE
        elif q_vals[0] < q_vals[1]:
            return Action.DEFECT
        
        # they are equal so random.
        return Action.COOPERATE if random() < 0.5 else Action.DEFECT

    def _update_q_values(self, history: List[Action], opp_history: List[Action]) -> None:

        new_state = self._construct_current_state(history, opp_history)
        reward = PAYOFF_MATRIX[history[-1]][opp_history[-1]][0] # calculate reward
        '''
            s = self._prev_state, s' = new_state (after taking action, history is updated so the state constructed is new)
            Q(s, a) = Q(s, a) + learning_rate * (reward + discount_rate * Q(s', a') - Q(s, a)) where a' is the action that returns maximum q-value from new_state.
        '''
        self._q_table[self._prev_state]  = self._q_table[self._prev_state] + self._learning_rate * (reward + self._discount_rate * max(self._q_table[new_state]) - max(self._q_table[self._prev_state]))

    def _save_q_table(self) -> None:

        pass
    
    '''
        State is returned in a oldest to newest ordering.
    '''
    def _construct_current_state(self, history: List[Action], opp_history: List[Action]) -> tuple[tuple[Action, Action]]:

        # construct a tuple of tuples containing pairs of Actions.
        return zip(history[-1 * self._len_history:], opp_history[-1 * self._len_history:])

    def _build_q_table(self, len_history: int) -> dict[tuple[tuple[Action, Action]], List[float]]:

        # TODO: update this so it initially checks if there is a file named q_values_table and loads the table from there. otherwise construct a new one.

        '''
            A Q-table holds the q values for environment states and actions. The table is 
            iteratively modified as the agent updates its q values. An example of q table is given
            below for history size 1. 

            State = (Previous action of Q-learning agent, Previous action of opponent)
            The q-values in the table below are what you would expect for a TFT agent.

            The first element in the list for each key is the q-value for cooperating given the history,
            meanwhile the second element is the q-value for defecting given history.

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
        '''
        
        q_table = {}
        vec = [0 for _ in range(len_history)]     # base_4 vector of length 4^history. The ith value represents the outcome of the ith game in history.
        final_vec = [-1 for _ in range(len_history)]
        while vec != final_vec:
            ''' 
                State space is constructed as follows:
                Initialise a base 4 vector with length len_history. The ith value in the vector represents the outcome of the ith previous game. 
                0 = (C, C), 1 = (C, D), 2 = (D, C), 3 = (D, D)
                As you increment the vector from 0 - (4^(h) - 1), each possible sequence of outcomes is constructed

                E.g., the vector 3212 represents the sequence ((D, D), (D, C), (C, D), (D, C))
            '''
            q_table[self._create_key(vec)] = [0, 0]
            vec = self._increment_vec(vec, len_history)

        return q_table

    def _create_key(self, vec: List[int]) -> tuple[tuple[Action, Action]]:

        ret = []
        for elem in vec:
            if elem == 0:
                ret.append((Action.COOPERATE, Action.COOPERATE))
            elif elem == 1:
                ret.append((Action.COOPERATE, Action.DEFECT))
            elif elem == 2:
                ret.append((Action.DEFECT, Action.COOPERATE))
            else:
                ret.append((Action.DEFECT, Action.DEFECT))
        
        return tuple(ret)

    def _increment_vec(self, vec: List[int], len_history: int) -> List[int]:

        curr = -1 
        while 1:
            if curr == -1 * (len(vec) + 1):
                # overflow, which means we have generated all possible states. Time to break loop.
                return [-1 for _ in range(len_history)]
            if vec[curr] + 1 == 4:
                vec[curr] = 0
                curr -= 1
            else:
                vec[curr] += 1
                break
        
        return vec


