from typing import List

from tournament.action import Action
from tournament.agent import Agent


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

    def __init__(
        self, deadlock_threshold: int = 3, randomness_threshold: int = 8
    ):
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
