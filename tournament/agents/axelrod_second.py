from collections import Counter
from typing import List, Optional

import numpy.random
from numpy.random import RandomState
from scipy.stats import chisquare
from tournament.action import Action
from tournament.agent import Agent
from tournament.match import PAYOFF_MATRIX

C, D = Action.COOPERATE, Action.DEFECT

class Champion(Agent):
    """
    Strategy submitted to Axelrod's second tournament by Danny Champion.
    This player cooperates on the first 10 moves and plays Tit for Tat for the
    next 15 more moves. After 25 moves, the program cooperates unless all the
    following are true: the other player defected on the previous move, the
    other player cooperated less than 60% and the random number between 0 and 1
    is greater that the other player's cooperation rate.
    Names:
    - Champion: [Axelrod1980b]_
    """

    def play_move(self, history: List[Action], opp_history: List[Action]):
        """Actual strategy definition that determines player's action."""
        current_round = len(history)
        # Cooperate for the first 10 turns
        if current_round < 10:
            return C
        # Mirror partner for the next phase
        if current_round < 25:
            return opp_history[-1]
        # Now cooperate unless all of the necessary conditions are true
        cnt = Counter(opp_history)
        num_d = cnt[Action.DEFECT]
        defection_prop = num_d / len(opp_history)
        if opp_history[-1] == D:
            r = RandomState().rand()
            if defection_prop >= max(0.4, r):
                return D
        return C


class Borufsen(Agent):
    """
    Strategy submitted to Axelrod's second tournament by Otto Borufsen
    (K32R), and came in third in that tournament.
    This player keeps track of the the opponent's responses to own behavior:
    - `cd_count` counts: Opponent cooperates as response to player defecting.
    - `cc_count` counts: Opponent cooperates as response to player cooperating.
    The player has a defect mode and a normal mode.  In defect mode, the
    player will always defect.  In normal mode, the player obeys the following
    ranked rules:
    1. If in the last three turns, both the player/opponent defected, then
       cooperate for a single turn.
    2. If in the last three turns, the player/opponent acted differently from
       each other and they're alternating, then change next defect to
       cooperate.  (Doesn't block third rule.)
    3. Otherwise, do tit-for-tat.
    Start in normal mode, but every 25 turns starting with the 27th turn,
    re-evaluate the mode.  Enter defect mode if any of the following
    conditions hold:
    - Detected random:  Opponent cooperated 7-18 times since last mode
      evaluation (or start) AND less than 70% of opponent cooperation was in
      response to player's cooperation, i.e.
      cc_count / (cc_count+cd_count) < 0.7
    - Detect defective:  Opponent cooperated fewer than 3 times since last mode
      evaluation.
    When switching to defect mode, defect immediately.  The first two rules for
    normal mode require that last three turns were in normal mode.  When starting
    normal mode from defect mode, defect on first move.
    Names:
    - Borufsen: [Axelrod1980b]_
    """

    def __init__(self):
        super().__init__()
        self.cd_counts, self.cc_counts = 0, 0
        self.mutual_defect_streak = 0
        self.echo_streak = 0
        self.flip_next_defect = False
        self.mode = "Normal"

    def try_return(self, to_return):
        """
        We put the logic here to check for the `flip_next_defect` bit here,
        and proceed like normal otherwise.
        """

        if to_return == C:
            return C
        # Otherwise look for flip bit.
        if self.flip_next_defect:
            self.flip_next_defect = False
            return C
        return D

    def play_move(self, history: List[Action], opp_history: List[Action]):
        """Actual strategy definition that determines player's action."""
        turn = len(history) + 1

        if turn == 1:
            return C

        # Update the response history.
        if turn >= 3:
            if opp_history[-1] == C:
                if history[-2] == C:
                    self.cc_counts += 1
                else:
                    self.cd_counts += 1

        # Check if it's time for a mode change.
        if turn > 2 and turn % 25 == 2:
            coming_from_defect = False
            if self.mode == "Defect":
                coming_from_defect = True

            self.mode = "Normal"
            coops = self.cd_counts + self.cc_counts

            # Check for a defective strategy
            if coops < 3:
                self.mode = "Defect"

            # Check for a random strategy
            if (8 <= coops <= 17) and self.cc_counts / coops < 0.7:
                self.mode = "Defect"

            self.cd_counts, self.cc_counts = 0, 0

            # If defect mode, clear flags
            if self.mode == "Defect":
                self.mutual_defect_streak = 0
                self.echo_streak = 0
                self.flip_next_defect = False

            # Check this special case
            if self.mode == "Normal" and coming_from_defect:
                return D

        # Proceed
        if self.mode == "Defect":
            return D
        else:
            assert self.mode == "Normal"

            # Look for mutual defects
            if history[-1] == D and opp_history[-1] == D:
                self.mutual_defect_streak += 1
            else:
                self.mutual_defect_streak = 0
            if self.mutual_defect_streak >= 3:
                self.mutual_defect_streak = 0
                self.echo_streak = 0  # Reset both streaks.
                return self.try_return(C)

            # Look for echoes
            # Fortran code defaults two turns back to C if only second turn
            my_two_back, opp_two_back = C, C
            if turn >= 3:
                my_two_back = history[-2]
                opp_two_back = opp_history[-2]
            if (
                history[-1] != opp_history[-1]
                and history[-1] == opp_two_back
                and opp_history[-1] == my_two_back
            ):
                self.echo_streak += 1
            else:
                self.echo_streak = 0
            if self.echo_streak >= 3:
                self.mutual_defect_streak = 0  # Reset both streaks.
                self.echo_streak = 0
                self.flip_next_defect = True

            # Tit-for-tat
            return self.try_return(opp_history[-1])


class Leyvraz(Agent):
    """
    Strategy submitted to Axelrod's second tournament by Fransois Leyvraz
    (K68R) and came in twelfth in that tournament.
    The strategy uses the opponent's last three moves to decide on an action
    based on the following ordered rules.
    1. If opponent Defected last two turns, then Defect with prob 75%.
    2. If opponent Defected three turns ago, then Cooperate.
    3. If opponent Defected two turns ago, then Defect.
    4. If opponent Defected last turn, then Defect with prob 50%.
    5. Otherwise (all Cooperations), then Cooperate.
    Names:
    - Leyvraz: [Axelrod1980b]_
    """

    def __init__(self):
        super().__init__()
        self.prob_coop = {
            (C, C, C): 1.0,
            (C, C, D): 0.5,  # Rule 4
            (C, D, C): 0.0,  # Rule 3
            (C, D, D): 0.25,  # Rule 1
            (D, C, C): 1.0,  # Rule 2
            (D, C, D): 1.0,  # Rule 2
            (D, D, C): 1.0,  # Rule 2
            (D, D, D): 0.25,  # Rule 1
        }

    def random_choice(self, p: float = 0.5):
        """
        Return C with probability `p`, else return D
        No random sample is carried out if p is 0 or 1.
        Parameters
        ----------
        p : float
            The probability of picking C
        Returns
        -------
        axelrod.Action
        """
        if p == 0:
            return D

        if p == 1:
            return C

        r = RandomState().rand()
        if r < p:
            return C
        return D

    def play_move(self, history: List[Action], opp_history: List[Action]):
        recent_history = [C, C, C]  # Default to C.
        for go_back in range(1, 4):
            if len(opp_history) >= go_back:
                recent_history[-go_back] = opp_history[-go_back]

        return self.random_choice(
            self.prob_coop[
                (recent_history[-3], recent_history[-2], recent_history[-1])
            ]
        )
