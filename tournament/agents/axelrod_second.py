import random
from collections import Counter
from typing import List

import numpy as np
from numpy.random import RandomState
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
        # Now cooperate unless all the necessary conditions are true
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
    This player keeps track of the opponent's responses to own behavior:
    - `cd_count` counts: Opponent cooperates as response to player defecting.
    - `cc_count` counts: Opponent cooperates as response to player cooperating.
    The player has a defect mode and a normal mode.  In defect mode, the
    player will always defect.  In normal mode, the player obeys the following
    ranked rules:
    1. If in the last three turns, both the player/opponent defected, then
       cooperate for a single turn.
    2. If in the last three turns, the player/opponent acted differently from
       each other, and they're alternating, then change next defect to
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
        # Otherwise, look for flip bit.
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
            self.prob_coop[(recent_history[-3], recent_history[-2], recent_history[-1])]
        )


class SecondByHarrington(Agent):
    """
    Strategy submitted to Axelrod's second tournament by Paul Harrington (K75R)
    and came in eighth in that tournament.

    This strategy has three modes:  Normal, Fair-weather, and Defect.  These
    mode names were not present in Harrington's submission.

    In Normal and Fair-weather modes, the strategy begins by:
    - Update history
    - Try to detect random opponent if turn is multiple of 15 and >=30.
    - Check if `burned` flag should be raised.
    - Check for Fair-weather opponent if turn is 38.

    Updating history means to increment the correct cell of the `move_history`.
    `move_history` is a matrix where the columns are the opponent's previous
    move and the rows are indexed by the combo of this player's and the
    opponent's moves two turns ago.  [The upper-left cell must be all
    Cooperations, but otherwise order doesn't matter.]  After we enter Defect
    mode, `move_history` won't be used again.

    If the turn is a multiple of 15 and >=30, then attempt to detect random.
    If random is detected, enter Defect mode and defect immediately.  If the
    player was previously in Defect mode, then do not re-enter.  The random
    detection logic is a modified Pearson's Chi Squared test, with some
    additional checks.  [More details in `detect_random` docstrings.]

    Some of this player's moves are marked as "generous."  If this player made
    a generous move two turns ago and the opponent replied with a Defect, then
    raise the `burned` flag.  This will stop certain generous moves later.

    The player mostly plays Tit-for-Tat for the first 36 moves, then defects on
    the 37th move.  If the opponent cooperates on the first 36 moves, and
    defects on the 37th move also, then enter Fair-weather mode and cooperate
    this turn.  Entering Fair-weather mode is extremely rare, since this can
    only happen if the opponent cooperates for the first 36 then defects
    unprovoked on the 37th.  (That is, this player's first 36 moves are also
    Cooperations, so there's nothing really to trigger an opponent Defection.)

    Next in Normal Mode:
    1. Check for defect and parity streaks.
    2. Check if cooperations are scheduled.
    3. Otherwise,
    - If turn < 37, Tit-for-Tat.
    - If turn = 37, defect, mark this move as generous, and schedule two
      more cooperations**.
    - If turn > 37, then if `burned` flag is raised, then Tit-for-Tat.
      Otherwise, Tit-for-Tat with probability 1 - `prob`.  And with
      probability `prob`, defect, schedule two cooperations, mark this move
      as generous, and increase `prob` by 5%.

    ** Scheduling two cooperations means to set `more_coop` flag to two.  If in
    Normal mode and no streaks are detected, then the player will cooperate and
    lower this flag, until hitting zero.  It's possible that the flag can be
    overwritten.  Notable on the 37th turn defect, this is set to two, but the
    38th turn Fair-weather check will set this.

    If the opponent's last twenty moves were defections, then defect this turn.
    Then check for a parity streak, by flipping the parity bit (there are two
    streaks that get tracked which are something like odd and even turns, but
    this flip bit logic doesn't get run every turn), then incrementing the
    parity streak that we're pointing to.  If the parity streak that we're
    pointing to is then greater than `parity_limit` then reset the streak and
    cooperate immediately.  `parity_limit` is initially set to five, but after
    it has been hit eight times, it decreases to three.  The parity streak that
    we're pointing to also gets incremented if in normal mode, and we defect but
    not on turn 38, unless we are defecting as the result of a defect streak.
    Note that the parity streaks resets but the defect streak doesn't.

    If `more_coop` >= 1, then we cooperate and lower that flag here, in Normal
    mode after checking streaks.  Still lower this flag if cooperating as the
    result of a parity streak or in Fair-weather mode.

    Then use the logic based on turn from above.

    In Fair-Weather mode after running the code from above, check if opponent
    defected last turn.  If so, exit Fair-Weather mode, and proceed THIS TURN
    with Normal mode.  Otherwise, cooperate.

    In Defect mode, update the `exit_defect_meter` (originally zero) by
    incrementing if opponent defected last turn and decreasing by three
    otherwise.  If `exit_defect_meter` is then 11, then set mode to Normal (for
    future turns), cooperate and schedule two more cooperations.  [Note that
    this move is not marked generous.]

    Names:
    - Harrington: [Axelrod1980b]_
    """

    def __init__(self):
        super().__init__()
        self.opp_D_count = 0
        self.mode = "Normal"
        self.recorded_defects = 0  # Count opponent defects after turn 1
        self.exit_defect_meter = 0  # When >= 11, then exit defect mode.
        self.coops_in_first_36 = None  # On turn 37, count cooperations in first 36
        self.was_defective = False  # Previously in Defect mode

        self.prob = 0.25  # After turn 37, probability that we'll defect

        self.move_history = np.zeros([4, 2])

        self.more_coop = 0  # This schedules cooperation for future turns
        # Initial last_generous_n_turns_ago to 3 because this counts up and
        # triggers a strategy change at 2.
        self.last_generous_n_turns_ago = 3  # How many tuns ago was a "generous" move
        self.burned = False

        self.defect_streak = 0
        self.parity_streak = [
            0,
            0,
        ]  # Counters that get (almost) alternatively incremented.
        self.parity_bit = 0  # Which parity_streak to increment
        self.parity_limit = 5  # When a parity streak hits this limit, alter strategy.
        self.parity_hits = 0  # Counts how many times a parity_limit was hit.
        # After hitting parity_hits 8 times, lower parity_limit to 3.

    def try_return(self, to_return, lower_flags=True, inc_parity=False):
        """
        This will return to_return, with some end-of-turn logic.
        """

        if lower_flags and to_return == C:
            # In most cases when Cooperating, we want to reduce the number that
            # are scheduled.
            self.more_coop -= 1
            self.last_generous_n_turns_ago += 1

        if inc_parity and to_return == D:
            # In some cases we increment the `parity_streak` that we're on when
            # we return a Defection.  In detect_parity_streak, `parity_streak`
            # counts opponent's Defections.
            self.parity_streak[self.parity_bit] += 1

        return to_return

    def calculate_chi_squared(self, turn):
        """
        Pearson's Chi Squared statistic = sum[ (E_i-O_i)^2 / E_i ], where O_i
        are the observed matrix values, and E_i is calculated as number (of
        defects) in the row times the number in the column over (total number
        in the matrix minus 1).  Equivalently, we expect (for an
        independent distribution) the total number of recorded turns times the
        portion in that row times the portion in that column.
        In this function, the statistic is non-standard in that it excludes
        summands where E_i <= 1.
        """

        denominator = turn - 2

        expected_matrix = (
            np.outer(self.move_history.sum(axis=1), self.move_history.sum(axis=0))
            / denominator
        )

        chi_squared = 0.0
        for i in range(4):
            for j in range(2):
                expect = expected_matrix[i, j]
                if expect > 1.0:
                    chi_squared += (expect - self.move_history[i, j]) ** 2 / expect

        return chi_squared

    def detect_random(self, turn):
        """
        We check if the top-left cell of the matrix (corresponding to all
        Cooperations) has over 80% of the turns.  In which case, we label
        non-random.
        Then we check if over 75% or under 25% of the opponent's turns are
        Defections.  If so, then we label as non-random.
        Otherwise, we calculate a modified Pearson's Chi Squared statistic on
        history, and returns True (is random) if and only if the statistic
        is less than or equal to 3.
        """

        denominator = turn - 2

        if self.move_history[0, 0] / denominator >= 0.8:
            return False
        if (
            self.recorded_defects / denominator < 0.25
            or self.recorded_defects / denominator > 0.75
        ):
            return False

        if self.calculate_chi_squared(turn) > 3:
            return False
        return True

    def detect_streak(self, last_move):
        """
        Return true if and only if the opponent's last twenty moves are defects.
        """

        if last_move == D:
            self.defect_streak += 1
        else:
            self.defect_streak = 0
        if self.defect_streak >= 20:
            return True
        return False

    def detect_parity_streak(self, last_move):
        """
        Switch which `parity_streak` we're pointing to and increment if the
        opponent's last move was a Defection.  Otherwise, reset the flag.  Then
        return true if and only if the `parity_streak` is at least
        `parity_limit`.
        This is similar to detect_streak with alternating streaks, except that
        these streaks get incremented elsewhere as well.
        """

        self.parity_bit = 1 - self.parity_bit  # Flip bit
        if last_move == D:
            self.parity_streak[self.parity_bit] += 1
        else:
            self.parity_streak[self.parity_bit] = 0
        if self.parity_streak[self.parity_bit] >= self.parity_limit:
            return True

    def play_move(self, history: List[Action], opp_history: List[Action]):
        """Actual strategy definition that determines player's action."""
        turn = len(history) + 1

        if turn == 1:
            return C

        self.opp_D_count += opp_history[-1].value - 1  # C = 1, D = 2

        if self.mode == "Defect":
            # There's a chance to exit Defect mode.
            if opp_history[-1] == D:
                self.exit_defect_meter += 1
            else:
                self.exit_defect_meter -= 3
            # If opponent has been mostly defecting.
            if self.exit_defect_meter >= 11:
                self.mode = "Normal"
                self.was_defective = True
                self.more_coop = 2
                return self.try_return(to_return=C, lower_flags=False)
            return self.try_return(D)

        # If not Defect mode, proceed to update history and check for random,
        # check if burned, and check if opponent's fair-weather.

        # If we haven't yet entered Defect mode
        if not self.was_defective:
            if turn > 2:
                if opp_history[-1] == D:
                    self.recorded_defects += 1

                # Column decided by opponent's last turn
                history_col = 1 if opp_history[-1] == D else 0
                # Row is decided by opponent's move two turns ago and our move
                # two turns ago.
                history_row = 1 if opp_history[-2] == D else 0
                if history[-2] == D:
                    history_row += 2
                self.move_history[history_row, history_col] += 1

            # Try to detect random opponent
            if turn % 15 == 0 and turn > 15:
                if self.detect_random(turn):
                    self.mode = "Defect"
                    return self.try_return(
                        D, lower_flags=False
                    )  # Lower_flags not used here.

        # If generous 2 turns ago and opponent defected last turn
        if self.last_generous_n_turns_ago == 2 and opp_history[-1] == D:
            self.burned = True

        # Only enter Fair-weather mode if the opponent Cooperated the first 37
        # turns then Defected on the 38th.
        if turn == 38 and opp_history[-1] == D and self.opp_D_count == 36:
            self.mode = "Fair-weather"
            return self.try_return(to_return=C, lower_flags=False)

        if self.mode == "Fair-weather":
            if opp_history[-1] == D:
                self.mode = "Normal"  # Post-Defect is not possible
                # Proceed with Normal mode this turn.
            else:
                # Never defect against a fair-weather opponent
                return self.try_return(C)

        # Continue with Normal mode

        # Check for streaks
        if self.detect_streak(opp_history[-1]):
            return self.try_return(D, inc_parity=True)

        if self.detect_parity_streak(opp_history[-1]):
            self.parity_streak[
                self.parity_bit
            ] = 0  # Reset `parity_streak` when we hit the limit.
            self.parity_hits += 1  # Keep track of how many times we hit the limit.
            if self.parity_hits >= 8:  # After 8 times, lower the limit.
                self.parity_limit = 3
            return self.try_return(
                C, inc_parity=True
            )  # Inc parity won't get used here.

        # If we have Cooperations scheduled, then Cooperate here.
        if self.more_coop >= 1:
            return self.try_return(C, lower_flags=True, inc_parity=True)

        if turn < 37:
            # Tit-for-Tat
            return self.try_return(opp_history[-1], inc_parity=True)

        if turn == 37:
            # Defect once on turn 37 (if no streaks)
            self.more_coop, self.last_generous_n_turns_ago = 2, 1
            return self.try_return(D, lower_flags=False)

        if self.burned or np.random.random() > self.prob:
            # Tit-for-Tat with probability 1-`prob`
            return self.try_return(opp_history[-1], inc_parity=True)

        # Otherwise Defect, Cooperate, Cooperate, and increase `prob`
        self.prob += 0.05
        self.more_coop, self.last_generous_n_turns_ago = 2, 1
        return self.try_return(D, lower_flags=False)


class SecondByWhiteK72R(Agent):
    # Cooperate for 10 times firstly
    # Cooperate if opponent Cooperates.
    # Otherwise, defect if and only if:
    #    floor(log(turn)) * opponent's DEFECTION >= turn

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        turn = len(history) + 1
        opp_defection_count = 0
        for i in range(len(opp_history)):
            opp_defection_count += 1 if (opp_history[i] == Action.DEFECT) else 0
        if turn <= 10 or opp_history[-1] == Action.COOPERATE:
            return Action.COOPERATE
        if np.floor(np.log(turn)) * opp_defection_count >= turn:
            return Action.DEFECT
        return Action.COOPERATE


class SecondByBlackK83R(Agent):
    # Cooperate for 5 times firstly
    # Then it calculates the number of opponent defects 'number_defects'
    # in the last five moves and Cooperates with probability 'prob_coop', where:
    # prob_coop[number_defects] = 1 - (number_defects^ 2 - 1) / 25

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if len(opp_history) < 5:
            return Action.COOPERATE
        opp_defection_count_l5 = 0
        for i in range(5):
            opp_defection_count_l5 += 1 if (opp_history[-5:][i] == Action.DEFECT) else 0
        prob_coop = {0: 1.0, 1: 1.0, 2: 0.88, 3: 0.68, 4: 0.4, 5: 0.04}
        if random.random() <= prob_coop[opp_defection_count_l5]:
            return Action.COOPERATE
        else:
            return Action.DEFECT


class SecondByTidemanAndChieruzzi(Agent):
    """
    Strategy submitted to Axelrod's second tournament by T. Nicolaus Tideman
    and Paula Chieruzzi (K84R) and came in ninth in that tournament.

    This strategy Cooperates if this player's score exceeds the opponent's
    score by at least `score_to_beat`.  `score_to_beat` starts at zero and
    increases by `score_to_beat_inc` every time the opponent's last two moves
    are a Cooperation and Defection in that order.  `score_to_beat_inc` itself
    increase by 5 every time the opponent's last two moves are a Cooperation
    and Defection in that order.

    Additionally, the strategy executes a "fresh start" if the following hold:
    - The strategy would Defect by score (difference less than `score_to_beat`)
    - The opponent did not Cooperate and Defect (in order) in the last two
      turns.
    - It's been at least 10 turns since the last fresh start.  Or since the
      match started if there hasn't been a fresh start yet.

    A "fresh start" entails two Cooperations and resetting scores,
    `scores_to_beat` and `scores_to_beat_inc`.

    Names:
    - TidemanAndChieruzzi: [Axelrod1980b]_
    """

    def __init__(self):
        super().__init__()
        self.score_diff = 0
        self.last_fresh_start = 0
        self.fresh_start = False
        self.score_to_beat = 0
        self.score_to_beat_inc = 0
        self.opp_D_count = 0

    def _fresh_start(self):
        """Give the opponent a fresh start by forgetting the past"""
        self.score_diff = 0
        self.score_to_beat = 0
        self.score_to_beat_inc = 0

    def play_move(self, history: List[Action], opp_history: List[Action]):
        """Actual strategy definition that determines player's action."""
        current_round = len(history) + 1

        if current_round == 1:
            return C

        self.opp_D_count += opp_history[-1].value - 1  # C = 1, D = 2
        # Calculate the scores.
        last_round = PAYOFF_MATRIX[(history[-1], opp_history[-1])]
        self.score_diff += last_round[0]
        self.score_diff -= last_round[1]

        # Check if we have recently given the strategy a fresh start.
        if self.fresh_start:
            self._fresh_start()
            self.last_fresh_start = current_round
            self.fresh_start = False
            return C  # Second cooperation

        opponent_CDd = False

        opponent_two_turns_ago = C  # Default value for second turn.
        if len(opp_history) >= 2:
            opponent_two_turns_ago = opp_history[-2]
        # If opponent's last two turns are C and D in that order.
        if opponent_two_turns_ago == C and opp_history[-1] == D:
            opponent_CDd = True
            self.score_to_beat += self.score_to_beat_inc
            self.score_to_beat_inc += 5

        # Cooperate if we're beating opponent by at least `score_to_beat`
        if self.score_diff >= self.score_to_beat:
            return C

        # Wait at least ten turns for another fresh start.
        if (not opponent_CDd) and current_round - self.last_fresh_start >= 10:
            # 50-50 split is based off the binomial distribution.
            N = len(opp_history)
            # std_dev = sqrt(N*p*(1-p)) where p is 1 / 2.
            std_deviation = (N ** (1 / 2)) / 2
            lower = N / 2 - 3 * std_deviation
            upper = N / 2 + 3 * std_deviation
            if self.opp_D_count <= lower or self.opp_D_count >= upper:
                # Opponent deserves a fresh start
                self.fresh_start = True
                return C  # First cooperation

        return D


class SecondByWmAdams(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:

        """
        Count # of defects, label it c_defect
        if c_defect equals 4, 7, or 9 => defect.
        if c_defect > 9 => defect after opponent defection with prob 0.5 ^(c_defect - 1). Otherwise, cooperate.
        """

        c_defect = opp_history.count(Action.DEFECT)

        if c_defect == 4 or c_defect == 7 or c_defect == 9:
            return Action.DEFECT

        if opp_history[-1] == Action.DEFECT and c_defect > 9:
            if random() <= 0.5 ** (c_defect - 1):
                return Action.DEFECT

        return Action.COOPERATE


class SecondByCave(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:

        """
        First, check if opponent is overly defective and defect if found. I.e., if they meet any of the following conditions:
        - turn > 39 and % defects > 0.39
        - turn > 29 and % defects > 0.65
        - turn > 19 and % defects > 0.79

        Else, cooperate if they cooperated last turn. If enemy defected, then either defect if opp has defected > 18 times or 50/50 chance.
        Note, cooperate on first move.
        """

        if not history:
            return Action.COOPERATE

        num_defects = opp_history.count(Action.DEFECT)
        percent_defect = num_defects / len(opp_history)
        if len(history) > 39 and percent_defect > 0.39:
            return Action.DEFECT
        if len(history) > 29 and percent_defect > 0.65:
            return Action.DEFECT
        if len(history) > 19 and percent_defect > 0.79:
            return Action.DEFECT

        if opp_history[-1] == Action.DEFECT:
            if num_defects > 18:
                return Action.DEFECT
            if random() < 0.5:
                return Action.DEFECT

        return Action.COOPERATE
