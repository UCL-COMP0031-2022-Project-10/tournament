import random
from typing import List

import numpy as np
from numpy.random import RandomState
from tournament.action import Action
from tournament.agent import Agent
from tournament.match import PAYOFF_MATRIX


class Champion(Agent):
    """
    This class implements the agent submitted by Danny Champion to Axelrod's second tournament.

    This agent cooperates on the first 10 moves and then plays TitForTat on the next 15 more moves.
    After 25 moves, the program cooperates unless all the following are true:
    - the other player defected on the previous move,
    - the other player cooperated less than 60% and
    - the random number between 0 and 1 is greater that the other player's cooperation rate.

    The implementation of this agent was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_second.py#L18
    """

    def __init__(self) -> None:
        super().__init__()

        self.defections = 0

    def play_move(self, history: List[Action], opp_history: List[Action]):
        current_round = len(history)
        if current_round > 0 and opp_history[-1] == Action.DEFECT:
            self.defections += 1

        # Cooperate for the first 10 turns
        if current_round < 10:
            return Action.COOPERATE

        # TFT next 15 turns
        if current_round < 25:
            return opp_history[-1]

        # Calculate defection rate
        defection_prop = self.defections / len(opp_history)
        # Check if all conditions are met
        if opp_history[-1] == Action.DEFECT:
            r = RandomState().rand()
            if defection_prop >= max(0.4, r):
                return Action.DEFECT

        return Action.COOPERATE


class Borufsen(Agent):
    """
    This class implements the agent submitted by Otto Borufsen to Axelrod's second tournament.

    The implementation of this agent was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_second.py#L606
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
        return in normal mode.
        """

        # If C, return C
        if to_return == Action.COOPERATE:
            return Action.COOPERATE
        # If D, check flip bit.
        # If flip, return C
        if self.flip_next_defect:
            self.flip_next_defect = False
            return Action.COOPERATE
        # If not flip, return D
        return Action.DEFECT

    def play_move(self, history: List[Action], opp_history: List[Action]):
        """plays a move."""
        turn = len(history) + 1

        # first time return C
        if turn == 1:
            return Action.COOPERATE

        # Update the response history.
        if turn >= 3:
            if opp_history[-1] == Action.COOPERATE:
                if history[-2] == Action.COOPERATE:
                    self.cc_counts += 1
                else:
                    self.cd_counts += 1

        # Check for mode change from the 27th turn every 25 turns.
        if turn > 2 and turn % 25 == 2:
            coming_from_defect = False
            if self.mode == "Defect":
                coming_from_defect = True

            self.mode = "Normal"
            coops = self.cd_counts + self.cc_counts

            # Detect defective.
            if coops < 3:
                self.mode = "Defect"

            # Detect random.
            if (8 <= coops <= 17) and self.cc_counts / coops < 0.7:
                self.mode = "Defect"

            self.cd_counts, self.cc_counts = 0, 0

            # If defect mode, clear flags
            if self.mode == "Defect":
                self.mutual_defect_streak = 0
                self.echo_streak = 0
                self.flip_next_defect = False

            #  When starting normal mode from defect mode, defect on first move.
            if self.mode == "Normal" and coming_from_defect:
                return Action.DEFECT

        # Proceed
        if self.mode == "Defect":
            return Action.DEFECT
        else:
            assert self.mode == "Normal"

            # update mutual defect streak
            if history[-1] == Action.DEFECT and opp_history[-1] == Action.DEFECT:
                self.mutual_defect_streak += 1
            else:
                self.mutual_defect_streak = 0

            # If in the last three turns, both the player/opponent defected, cooperate for a single turn.
            if self.mutual_defect_streak >= 3:
                self.mutual_defect_streak = 0
                self.echo_streak = 0  # Reset both streaks.
                return self.try_return(Action.COOPERATE)

            # Look for echoes
            my_two_back, opp_two_back = Action.COOPERATE, Action.COOPERATE
            if turn >= 3:
                my_two_back = history[-2]
                opp_two_back = opp_history[-2]

            # update echo streak
            if (
                history[-1] != opp_history[-1]
                and history[-1] == opp_two_back
                and opp_history[-1] == my_two_back
            ):
                self.echo_streak += 1
            else:
                self.echo_streak = 0

            # If in the last three turns, the player/opponent echoed alternatingly, change next defect to cooperate.
            if self.echo_streak >= 3:
                self.mutual_defect_streak = 0  # Reset both streaks.
                self.echo_streak = 0
                self.flip_next_defect = True

            # Tit-for-tat
            return self.try_return(opp_history[-1])


class Leyvraz(Agent):
    """
    This class implements the agent submitted by Francois Leyvraz to Axelrod's second tournament.

    The strategy uses the opponent's last three moves to decide on an action
    based on the following ordered rules.
    1. If opponent Defected last two turns, then Defect with prob 75%.
    2. If opponent Defected three turns ago, then Cooperate.
    3. If opponent Defected two turns ago, then Defect.
    4. If opponent Defected last turn, then Defect with prob 50%.
    5. Otherwise (all Cooperations), then Cooperate.

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_second.py#L1534
    """

    def __init__(self):
        super().__init__()
        self.prob_coop = {
            # Rule 1
            (Action.COOPERATE, Action.DEFECT, Action.DEFECT): 0.25,
            (Action.DEFECT, Action.DEFECT, Action.DEFECT): 0.25,
            # Rule 2
            (Action.DEFECT, Action.COOPERATE, Action.COOPERATE): 1.0,
            (Action.DEFECT, Action.COOPERATE, Action.DEFECT): 1.0,
            (Action.DEFECT, Action.DEFECT, Action.COOPERATE): 1.0,
            # Rule 3
            (Action.COOPERATE, Action.DEFECT, Action.COOPERATE): 0.0,
            # Rule 4
            (Action.COOPERATE, Action.COOPERATE, Action.DEFECT): 0.5,
            # Rule 5
            (Action.COOPERATE, Action.COOPERATE, Action.COOPERATE): 1.0,
        }

    def random_choice(self, p: float = 0.5):
        """
        Return action according to cooperation probability p.
        """
        if p == 0:
            return Action.DEFECT

        if p == 1:
            return Action.COOPERATE

        r = RandomState().rand()
        if r < p:
            return Action.COOPERATE
        return Action.DEFECT

    def play_move(self, history: List[Action], opp_history: List[Action]):
        recent_history = [
            Action.COOPERATE,
            Action.COOPERATE,
            Action.COOPERATE,
        ]  # Default to C.
        for go_back in range(1, 4):
            if len(opp_history) >= go_back:
                recent_history[-go_back] = opp_history[-go_back]

        return self.random_choice(
            self.prob_coop[(recent_history[-3], recent_history[-2], recent_history[-1])]
        )


class Harrington(Agent):
    """
    This class implements the strategy submitted by Paul Harrington to Axelrod's second tournament.

    This agent implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_second.py#L1027

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

        if lower_flags and to_return == Action.COOPERATE:
            # In most cases when Cooperating, we want to reduce the number that
            # are scheduled.
            self.more_coop -= 1
            self.last_generous_n_turns_ago += 1

        if inc_parity and to_return == Action.DEFECT:
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

        if last_move == Action.DEFECT:
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
        if last_move == Action.DEFECT:
            self.parity_streak[self.parity_bit] += 1
        else:
            self.parity_streak[self.parity_bit] = 0
        if self.parity_streak[self.parity_bit] >= self.parity_limit:
            return True

    def play_move(self, history: List[Action], opp_history: List[Action]):
        """Actual strategy definition that determines player's action."""
        turn = len(history) + 1

        if turn == 1:
            return Action.COOPERATE

        self.opp_D_count += opp_history[-1].value - 1  # C = 1, D = 2

        if self.mode == "Defect":
            # There's a chance to exit Defect mode.
            if opp_history[-1] == Action.DEFECT:
                self.exit_defect_meter += 1
            else:
                self.exit_defect_meter -= 3
            # If opponent has been mostly defecting.
            if self.exit_defect_meter >= 11:
                self.mode = "Normal"
                self.was_defective = True
                self.more_coop = 2
                return self.try_return(to_return=Action.COOPERATE, lower_flags=False)
            return self.try_return(Action.DEFECT)

        # If not Defect mode, proceed to update history and check for random,
        # check if burned, and check if opponent's fair-weather.

        # If we haven't yet entered Defect mode
        if not self.was_defective:
            if turn > 2:
                if opp_history[-1] == Action.DEFECT:
                    self.recorded_defects += 1

                # Column decided by opponent's last turn
                history_col = 1 if opp_history[-1] == Action.DEFECT else 0
                # Row is decided by opponent's move two turns ago and our move
                # two turns ago.
                history_row = 1 if opp_history[-2] == Action.DEFECT else 0
                if history[-2] == Action.DEFECT:
                    history_row += 2
                self.move_history[history_row, history_col] += 1

            # Try to detect random opponent
            if turn % 15 == 0 and turn > 15:
                if self.detect_random(turn):
                    self.mode = "Defect"
                    return self.try_return(
                        Action.DEFECT, lower_flags=False
                    )  # Lower_flags not used here.

        # If generous 2 turns ago and opponent defected last turn
        if self.last_generous_n_turns_ago == 2 and opp_history[-1] == Action.DEFECT:
            self.burned = True

        # Only enter Fair-weather mode if the opponent Cooperated the first 37
        # turns then Defected on the 38th.
        if turn == 38 and opp_history[-1] == Action.DEFECT and self.opp_D_count == 36:
            self.mode = "Fair-weather"
            return self.try_return(to_return=Action.COOPERATE, lower_flags=False)

        if self.mode == "Fair-weather":
            if opp_history[-1] == Action.DEFECT:
                self.mode = "Normal"  # Post-Defect is not possible
                # Proceed with Normal mode this turn.
            else:
                # Never defect against a fair-weather opponent
                return self.try_return(Action.COOPERATE)

        # Continue with Normal mode

        # Check for streaks
        if self.detect_streak(opp_history[-1]):
            return self.try_return(Action.DEFECT, inc_parity=True)

        if self.detect_parity_streak(opp_history[-1]):
            self.parity_streak[
                self.parity_bit
            ] = 0  # Reset `parity_streak` when we hit the limit.
            self.parity_hits += 1  # Keep track of how many times we hit the limit.
            if self.parity_hits >= 8:  # After 8 times, lower the limit.
                self.parity_limit = 3
            return self.try_return(
                Action.COOPERATE, inc_parity=True
            )  # Inc parity won't get used here.

        # If we have Cooperations scheduled, then Cooperate here.
        if self.more_coop >= 1:
            return self.try_return(Action.COOPERATE, lower_flags=True, inc_parity=True)

        if turn < 37:
            # TitForTat
            return self.try_return(opp_history[-1], inc_parity=True)

        if turn == 37:
            # Defect once on turn 37 (if no streaks)
            self.more_coop, self.last_generous_n_turns_ago = 2, 1
            return self.try_return(Action.DEFECT, lower_flags=False)

        if self.burned or np.random.random() > self.prob:
            # TitForTat with probability 1-`prob`
            return self.try_return(opp_history[-1], inc_parity=True)

        # Otherwise Defect, Cooperate, Cooperate, and increase `prob`
        self.prob += 0.05
        self.more_coop, self.last_generous_n_turns_ago = 2, 1
        return self.try_return(Action.DEFECT, lower_flags=False)


class White(Agent):
    """
    This class implements the agent submitted by Edward White to Axelrod's second tournament.

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_second.py#L1589
    """

    # Cooperate for 10 times firstly
    # Cooperate if opponent Cooperates.
    # Otherwise, defect if and only if:
    #    floor(log(turn)) * opponent's DEFECTION >= turn

    def __init__(self) -> None:
        super().__init__()

        self.defections = 0

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        turn = len(history) + 1

        if opp_history and opp_history[-1] == Action.DEFECT:
            self.defections += 1

        if turn <= 10 or opp_history[-1] == Action.COOPERATE:
            return Action.COOPERATE

        if np.floor(np.log(turn)) * self.defections >= turn:
            return Action.DEFECT

        return Action.COOPERATE


class SecondByBlackK83R(Agent):
    """
    This class implements the agent submitted by Paul Black to Axelrod's second tournament.

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_second.py#L1625
    """

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if len(opp_history) < 5:
            return Action.COOPERATE

        opp_defection_count = 0
        for i in range(5):
            if opp_history[-5:][i] == Action.DEFECT:
                opp_defection_count += 1

        prob_coop = {0: 1.0, 1: 1.0, 2: 0.88, 3: 0.68, 4: 0.4, 5: 0.04}

        return (
            Action.COOPERATE
            if random.random() <= prob_coop[opp_defection_count]
            else Action.DEFECT
        )


class TidemanAndChieruzzi2(Agent):
    """
    This class implements the agent submitted by Tideman and Chieruzzi to Axelrod's second tournament.

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_second.py#L1385
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
            return Action.COOPERATE

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
            return Action.COOPERATE  # Second cooperation

        opponent_CDd = False

        opponent_two_turns_ago = Action.COOPERATE  # Default value for second turn.
        if len(opp_history) >= 2:
            opponent_two_turns_ago = opp_history[-2]
        # If opponent's last two turns are C and D in that order.
        if (
            opponent_two_turns_ago == Action.COOPERATE
            and opp_history[-1] == Action.DEFECT
        ):
            opponent_CDd = True
            self.score_to_beat += self.score_to_beat_inc
            self.score_to_beat_inc += 5

        # Cooperate if we're beating opponent by at least `score_to_beat`
        if self.score_diff >= self.score_to_beat:
            return Action.COOPERATE

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
                return Action.COOPERATE  # First cooperation

        return Action.DEFECT


class Adams(Agent):
    """
    This class implements the agent submitted by William Adams to Axelrod's second tournament.

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_second.py#L819
    """

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if not history:
            return Action.COOPERATE

        c_defect = opp_history.count(Action.DEFECT)

        if c_defect == 4 or c_defect == 7 or c_defect == 9:
            return Action.DEFECT

        if opp_history[-1] == Action.DEFECT and c_defect > 9:
            if random.random() <= 0.5 ** (c_defect - 1):
                return Action.DEFECT

        return Action.COOPERATE


class Cave(Agent):
    """
    This class implements the agent submitted by Rob Cave to Axelrod's second tournament.

    First, check if opponent is overly defective and defect if found, i.e. if they meet any of the following conditions:
    - turn > 39 and % defects > 0.39
    - turn > 29 and % defects > 0.65
    - turn > 19 and % defects > 0.79

    Else, cooperate if they cooperated last turn. If the opponent defected, then either defect if opp has defected > 18 times or 50/50 chance.
    Note: cooperate on first move.

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_second.py#L762
    """

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
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
            if random.random() < 0.5:
                return Action.DEFECT

        return Action.COOPERATE


class GraaskampAndKatzen(Agent):
    """
    This class implements the agent submitted by Jim Graaskamp and Ken Katzen to Axelrod's second tournament.

    Play TitForTat at first and track its own score.  At select checkpoints,
    check for a high score.  Defect forever if:
    - On move 11, score < 23
    - On move 21, score < 53
    - On move 31, score < 83
    - On move 41, score < 113
    - On move 51, score < 143
    - On move 101, score < 293

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_second.py#L859
    """

    def __init__(self):
        super().__init__()
        self.own_score = 0
        self.mode = "Normal"

    def update_score(self, history: List[Action], opp_history: List[Action]):
        own_last_move = history[-1]
        opp_last_move = opp_history[-1]
        if own_last_move == opp_last_move:
            if own_last_move is Action.COOPERATE:
                self.own_score += 3
            else:
                self.own_score += 1
        else:
            if own_last_move is Action.COOPERATE:
                self.own_score += 0
            else:
                self.own_score += 5

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if self.mode == "Defect":
            return Action.DEFECT

        turn = len(history) + 1
        if turn == 1:
            return Action.COOPERATE

        self.update_score(history, opp_history)

        if (
            turn == 11
            and self.own_score < 23
            or turn == 21
            and self.own_score < 53
            or turn == 31
            and self.own_score < 83
            or turn == 41
            and self.own_score < 113
            or turn == 51
            and self.own_score < 143
            or turn == 101
            and self.own_score < 293
        ):
            self.mode = "Defect"
            return Action.DEFECT

        return opp_history[-1]


class Weiner(Agent):
    """
    This class implements the agent submitted by Herb Weiner to Axelrod's second tournament.

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_second.py#L932
    """

    def __init__(self):
        super().__init__()
        self.forgive_flag = False
        self.grudge = 0
        self.defect_padding = 0
        self.last_twelve = [0] * 12
        self.lt_index = 0  # Circles around last_twelve

    def try_return(self, to_return):
        """
        We put the logic here to check for the defective override.
        """

        if np.sum(self.last_twelve) >= 5:
            return Action.DEFECT
        return to_return

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        """Actual strategy definition that determines player's action."""
        if len(opp_history) == 0:
            return Action.COOPERATE

        # Update history, lag 1.
        if len(opp_history) >= 2:
            self.last_twelve[self.lt_index] = 0
            if opp_history[-2] == Action.DEFECT:
                self.last_twelve[self.lt_index] = 1
            self.lt_index = (self.lt_index + 1) % 12

        if self.forgive_flag:
            self.forgive_flag = False
            self.defect_padding = 0
            if self.grudge < len(history) + 1 and opp_history[-1] == Action.DEFECT:
                # Then override
                self.grudge += 20
                return self.try_return(Action.COOPERATE)
            else:
                return self.try_return(opp_history[-1])
        else:
            # See if forgive_flag should be raised
            if opp_history[-1] == Action.DEFECT:
                self.defect_padding += 1
            else:
                if self.defect_padding % 2 == 1:
                    self.forgive_flag = True
                self.defect_padding = 0

            return self.try_return(opp_history[-1])
