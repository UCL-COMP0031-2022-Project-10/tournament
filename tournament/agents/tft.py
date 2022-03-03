from random import random
from typing import List

from tournament.action import Action
from tournament.agent import Agent
from tournament.match import PAYOFF_MATRIX

C, D = Action.COOPERATE, Action.DEFECT


class TitForTat(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        # Cooperate initially
        if not opp_history:
            return Action.COOPERATE

        # Play the opponent's last action
        return opp_history[-1]


class OmegaTFT(Agent):
    """OmegaTFT modifies Tit For Tat in two ways:
    - checks for deadlock loops of alternating rounds of (C, D) and (D, C),
    and attempting to break them
    - uses a more sophisticated retaliation mechanism that is noise tolerant
    Names:
    - OmegaTFT: [Slany2007]_
    """

    def __init__(self, deadlock_threshold: int = 3, randomness_threshold: int = 8):
        """
        deadlock_threshold: the threshold for deadlock detection.
        randomness_threshold: the threshold for randomness detection.
        deadlock_counter: the number of consecutive rounds of (C, D) and (D, C)
        randomness_counter: the number of times the opponent changes behavior
        """
        super().__init__()
        self.deadlock_threshold = deadlock_threshold
        self.randomness_threshold = randomness_threshold
        self.randomness_counter = 0
        self.deadlock_counter = 0

    def play_move(self, history: List[Action], opp_history: List[Action]):
        """
        Plays a move.
        """
        # Cooperate on the first move
        if not opp_history:
            return Action.COOPERATE
        # TFT on round 2
        if len(history) == 1:
            return opp_history[-1]

        # If deadlocked, break the deadlock by cooperating
        if self.deadlock_counter >= self.deadlock_threshold:
            move = Action.COOPERATE
            if self.deadlock_counter == self.deadlock_threshold:
                self.deadlock_counter = self.deadlock_threshold + 1
            else:
                self.deadlock_counter = 0
        else:
            # Update counters
            if opp_history[-2:] == [Action.COOPERATE, Action.COOPERATE]:
                self.randomness_counter -= 1
            # If the opponent's move changed, increase the counter
            if opp_history[-2] != opp_history[-1]:
                self.randomness_counter += 1
            # If the opponent's last move differed from mine,
            # increase the counter
            if history[-1] != opp_history[-1]:
                self.randomness_counter += 1
            # Compare counts to thresholds
            # If randomness_counter exceeds threshold, switch to ALL D
            if self.randomness_counter >= self.randomness_threshold:
                move = Action.DEFECT
            else:
                # TFT
                move = opp_history[-1]
                # Check for deadlock
                if opp_history[-2] != opp_history[-1]:
                    self.deadlock_counter += 1
                else:
                    self.deadlock_counter = 0
        return move


# defect on opponent's two consecutive defection
class TFTT(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if len(opp_history) >= 2 and (
            opp_history[-1] == Action.DEFECT and opp_history[-2] == Action.DEFECT
        ):
            return Action.DEFECT
        else:
            return Action.COOPERATE


# defect twice on opponent's a single defection
class TTFT(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if (
            (not opp_history)
            or (len(opp_history) == 1 and opp_history[-1] == Action.COOPERATE)
            or (
                len(opp_history) >= 2
                and opp_history[-1] == Action.COOPERATE
                and opp_history[-2] == Action.COOPERATE
            )
        ):
            return Action.COOPERATE
        else:
            return Action.DEFECT


# TFT with two differences:
# (1) an additional defection for each time the opponent defects
# (2) having retaliated, cooperate twice
class GradualTFT(Agent):
    def __init__(self) -> None:
        super().__init__()

        self.defections = 0
        self.opp_defections = 0

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        # Cooperate initially
        if not opp_history:
            return Action.COOPERATE

        if history[-1] == Action.DEFECT:
            self.defections += 1

        if opp_history[-1] == Action.DEFECT:
            self.opp_defections += 1

        if len(opp_history) == 1 and opp_history[-1] == Action.DEFECT:
            return Action.DEFECT

        if len(opp_history) == 1 and opp_history[-1] == Action.COOPERATE:
            return Action.COOPERATE

        should_defect_total = 0
        for i in range(self.opp_defections):
            should_defect_total += i + 1

        # counting where we are in the retaliation series
        cur_retaliation_series_count = 0
        retaliation_to_complete_cur_series = 0
        copy_self_defect_count = self.defections
        while copy_self_defect_count > 0:
            cur_retaliation_series_count += 1
            copy_self_defect_count -= cur_retaliation_series_count
            retaliation_to_complete_cur_series += cur_retaliation_series_count

        # if we have NOT finished current retaliation series
        if self.defections < retaliation_to_complete_cur_series:
            return Action.DEFECT

        # to cooperate before we retaliate again
        elif not (history[-1] == Action.COOPERATE and history[-2] == Action.COOPERATE):
            return Action.COOPERATE

        # if we have NOT retaliated expected rounds
        elif self.defections < should_defect_total:
            return Action.DEFECT

        else:
            return Action.COOPERATE


# Following a defection, cooperate with a probability
class GenerousTFT(Agent):
    R = PAYOFF_MATRIX[(C, C)][0]
    T = PAYOFF_MATRIX[(D, C)][0]
    S = PAYOFF_MATRIX[(C, D)][0]
    P = PAYOFF_MATRIX[(D, D)][0]
    generosity = min(1 - (T - R) / (R - S), (R - P) / (T - P))

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        # Cooperate initially
        if not opp_history or opp_history[-1] == Action.COOPERATE:
            return Action.COOPERATE

        return Action.COOPERATE if random() < self.generosity else Action.DEFECT
