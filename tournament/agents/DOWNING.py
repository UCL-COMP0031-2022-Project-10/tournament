from typing import List, Tuple

from tournament.action import Action
from tournament.agent import Agent 

class Downing(Agent):

    def __init__(self):

        self._num_coop_following_coop = 0 # num of times opp has cooperated after Downing has cooperated. 
        self._num_coop_following_defect = 0 # num of times opp has cooperated after Downing has defected. 

    def _calc_conditional_probs(self, history: List[Agent]) -> Tuple[float, float]:

        alpha = self._num_coop_following_coop / (history.count(Action.COOPERATE) + 1) # add 1 to remove divide by zero error. We assume in the nonexistent round 0, Downing cooperated.
        beta = self._num_coop_following_defect / (history.count(Action.DEFECT)) 
        
        return (alpha, beta)


    def play_move(self, history: List[Agent], opp_history: List[Agent]) -> Action:
        
        # Calc P(C_o | C_s) = Prob(Opp cooperates | Downing cooperated previous turn) = alpha
        #      P(C_o | D_s) = Prob(Opp cooperates | Downing defected previous turn) = beta
        # R = reward (3), T = temptation (5), S = sucker (0), P = Punishment (1).
        # Expected Value for Cooperating (EV_C) = P(C_o | C_s) * R + (1 - P(C_o | C_s)) * S 
        # Expected Value for Defecting (EV_D) = P(C_o | D_s) * T + (1 - P(C_o | D_s)) * P
        # If EV_C > EV_D => Cooperate. If EV_D > EV_C => Defect. If EV_D = EV_C, do opposite of last action that Downing executed.
        # Downing has pessimistic assumption that starting probabilities are 0.5 each. Consequently, Downing always defects on first two turns.

        if len(history) == 0:
            return Action.DEFECT
        elif len(history) == 1:
            if opp_history[0] == Action.COOPERATE:
                self._num_coop_following_defect += 1
            return Action.DEFECT

        if opp_history[-1] == Action.COOPERATE and history[-2] == Action.COOPERATE:
            self._num_coop_following_coop += 1
        if opp_history[-1] == Action.COOPERATE and history[-2] == Action.DEFECT:
            self._num_coop_following_defect += 1

        alpha, beta = self._calc_conditional_probs(history)
        ev_c = alpha * 3 + (1 - alpha) * 0
        ev_d = beta * 5 + (1 - beta) * 1
        if ev_c > ev_d:
            return Action.COOPERATE
        elif ev_d > ev_c:
            return Action.DEFECT
        return Action.COOPERATE if history[-1] == Action.DEFECT else Action.DEFECT