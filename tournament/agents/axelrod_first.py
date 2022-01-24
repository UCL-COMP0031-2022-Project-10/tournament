from collections import Counter
from typing import List, Optional

import numpy.random
from numpy.random import RandomState
from scipy.stats import chisquare
from tournament.action import Action
from tournament.agent import Agent

C, D = Action.COOPERATE, Action.DEFECT


class Davis(Agent):
    """
    Submitted to Axelrod's first tournament by Morton Davis.

    The description written in [Axelrod1980]_ is:

    > "A player starts by cooperating for 10 rounds then plays Grudger,
    > defecting if at any point the opponent has defected."

    This strategy came 8th in Axelrod's original tournament.

    Names:

    - Davis: [Axelrod1980]_
    """

    def __init__(self, rounds_to_cooperate: int = 10):
        """
        rounds_to_cooperate: The number of rounds to play C.
        """
        super().__init__()
        self._rounds_to_cooperate = rounds_to_cooperate

    def play_move(self, history: List[Action], opp_history: List[Action]):
        """
        Begins by playing C, then plays D for the remaining rounds if the opponent ever plays D.
        """
        if len(history) < self._rounds_to_cooperate:
            # print("Davis: playing C")
            return Action.COOPERATE
        if opp_history and Action.DEFECT in opp_history:
            # print("Davis: playing D")
            return Action.DEFECT
        # print("Davis: playing C")
        return Action.COOPERATE


class Graaskamp(Agent):
    """
    Submitted to Axelrod's first tournament by James Graaskamp.

    The description written in [Axelrod1980]_ is:

    > This rule plays tit-for-tat for 50 moves, defects on move 51, and then
    > plays 5 more moves of tit-for-tat. A check is then made to see if the player
    > seems to be RANDOM, in which case it defects from then on. A check is also
    > made to see if the other is TIT FOR TAT, ANALOGY (a program from the
    > preliminary tournament), and its own twin, in which case it plays tit-for-tat
    > Otherwise, it randomly defects every 5 to 15 moves, hoping that enough
    > trust has been built up so that the other player will not notice these
    > defections.:

    This is implemented as:

    1. Plays Tit For Tat for the first 50 rounds;
    2. Defects on round 51;
    3. Plays 5 further rounds of Tit For Tat;
    4. A check is then made to see if the opponent is playing randomly in which
       case it defects for the rest of the game. This is implemented with a chi
       squared test.
    5. The strategy also checks to see if the opponent is playing Tit For Tat or
       a clone of itself. If
       so it plays Tit For Tat. If not it cooperates and randomly defects every 5
       to 15 moves.

    Note that there is no information about 'Analogy' available thus Step 5 is
    a "best possible" interpretation of the description in the paper.
    Furthermore, the test for the clone is implemented as checking that both
    players have played the same moves for the entire game. This is unlikely to
    be the original approach but no further details are available.

    This strategy came 9th in Axelrod’s original tournament.

    Names:

    - Graaskamp: [Axelrod1980]_
    """

    def __init__(self, alpha: float = 0.05):
        """
        alpha: the significant level of p-value from chi-squared test.
        """
        super().__init__()
        self.alpha = alpha
        self.opponent_is_random = False
        self.next_random_defection_turn = None  # type: Optional[int]

    def play_move(self, history: List[Action], opp_history: List[Action]):
        """
        Plays a move.
        """
        # Play TFT in the first 56 turns
        if len(history) < 56:
            # Defect on the 51st turn
            if len(history) == 50:
                # print("Graaskamp: playing D")
                return Action.DEFECT

            # Cooperate initially
            if not opp_history:
                # print("Graaskamp: playing C")
                return Action.COOPERATE

            # Play the opponent's last action
            # print("Graaskamp: playing " + str(opp_history[-1]))
            return opp_history[-1]

        cnt = Counter(opp_history)
        num_c = cnt[Action.COOPERATE]
        num_d = cnt[Action.DEFECT]

        # Check if opponent is random
        p_value = chisquare([num_c, num_d]).pvalue
        self.opponent_is_random = (p_value >= self.alpha) or self.opponent_is_random

        # If so, defect for the rest of the game
        if self.opponent_is_random:
            # print("Graaskamp: playing D")
            return Action.DEFECT

        # Check if opponent is Tit For Tat or a clone of itself
        if (
            all(opp_history[i] == history[i - 1] for i in range(1, len(history)))
            or opp_history == history
        ):
            # If so, play TFT
            # print("Graaskamp: playing " + str(opp_history[-1]))
            return opp_history[-1]

        # Otherwise, randomly defect every 5 to 15 moves
        if self.next_random_defection_turn is None:
            self.next_random_defection_turn = RandomState().randint(5, 15) + len(
                history
            )

        if len(history) == self.next_random_defection_turn:
            self.next_random_defection_turn = RandomState().randint(5, 15) + len(
                history
            )
            # print("Graaskamp: playing D")
            return Action.DEFECT

        # print("Graaskamp: playing C")
        return Action.COOPERATE


class Shubik(Agent):
    """
    Submitted to Axelrod's first tournament by Martin Shubik.
    The description written in [Axelrod1980]_ is:
    > This rule cooperates until the other defects, and then defects once. If
    > the other defects again after the rule's cooperation is resumed, the rule
    > defects twice. In general, the length of retaliation is increased by one for
    > each departure from mutual cooperation. This rule is described with its
    > strategic implications in Shubik (1970). Further treatment of its is given
    > in Taylor (1976).
    There is some room for interpretation as to how the strategy reacts to a
    defection on the turn where it starts to cooperate once more. In Shubik
    (1970) the strategy is described as:
    > "I will play my move 1 to begin with and will continue to do so, so long
    > as my information shows that the other player has chosen his move 1. If my
    > information tells me he has used move 2, then I will use move 2 for the
    > immediate k subsequent periods, after which I will resume using move 1. If
    > he uses his move 2 again after I have resumed using move 1, then I will
    > switch to move 2 for the k + 1 immediately subsequent periods . . . and so
    > on, increasing my retaliation by an extra period for each departure from the
    > (1, 1) steady state."
    This is interpreted as:
    The player cooperates, if when it is cooperating, the opponent defects it
    defects for k rounds. After k rounds it starts cooperating again and
    increments the value of k if the opponent defects again.
    This strategy came 5th in Axelrod's original tournament.
    Names:
    - Shubik: [Axelrod1980]_
    """

    def __init__(self):
        super().__init__()
        self.is_retaliating = False
        self.retaliation_length = 0
        self.retaliation_remaining = 0

    def _decrease_retaliation_counter(self):
        """
        Lower the remaining owed retaliation count and flip to non-retaliate
        if the count drops to zero.
        """
        if self.is_retaliating:
            self.retaliation_remaining -= 1
            if self.retaliation_remaining == 0:
                self.is_retaliating = False

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if not opp_history:
            return Action.COOPERATE

        if self.is_retaliating:
            self._decrease_retaliation_counter()
            return Action.DEFECT

        if opp_history[-1] == Action.DEFECT and history[-1] == Action.COOPERATE:
            self.is_retaliating = True
            self.retaliation_length += 1
            self.retaliation_remaining = self.retaliation_length
            self._decrease_retaliation_counter()
            return Action.DEFECT

        return Action.COOPERATE


class SteinAndRapoport(Agent):
    """
    Submitted to Axelrod's first tournament by William Stein and Amnon Rapoport.
    The description written in [Axelrod1980]_ is:
    > This rule plays tit-for-tat except that it cooperates on the first four
    > moves, it defects on the last two moves, and every fifteen moves it checks
    > to see if the opponent seems to be playing randomly. This check uses a
    > chi-squared test of the other's transition probabilities and also checks for
    > alternating moves of CD and DC.
    This is implemented as follows:
    1. It cooperates for the first 4 moves.
    2. It defects on the last 2 moves.
    3. Every 15 moves it makes use of a `chi-squared
       test <http://en.wikipedia.org/wiki/Chi-squared_test>`_ to check if the
       opponent is playing randomly. If so it defects.
    This strategy came 6th in Axelrod's original tournament.
    Names:
    - SteinAndRapoport: [Axelrod1980]_
    """

    def __init__(self, alpha: float = 0.05):
        """
        alpha: float
            The significant level of p-value from chi-squared test with
            alpha == 0.05 by default.
        """
        super().__init__()
        self.alpha = alpha
        self.opponent_is_random = False

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        round_number = len(history) + 1

        # First 4 moves
        if round_number < 5:
            return Action.COOPERATE

        # For first 15 rounds tit-for-tat as we do not know opponents strategy
        elif round_number < 15:
            return opp_history[-1]

        if round_number % 15 == 0:
            cnt = Counter(opp_history)
            num_c = cnt[Action.COOPERATE]
            num_d = cnt[Action.DEFECT]
            p_value = chisquare([num_c, num_d]).pvalue
            self.opponent_is_random = p_value >= self.alpha

        if self.opponent_is_random:
            # Defect if opponent plays randomly
            return Action.DEFECT
        else:  # TitForTat if opponent plays not randomly
            return opp_history[-1]


class Grudger(Agent):
    def __init__(self):
        super().__init__()
        self.is_retaliation = False

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if not opp_history:
            return Action.COOPERATE

        if self.is_retaliation is True:
            return Action.DEFECT

        if opp_history[-1] == Action.DEFECT:
            self.is_retaliation = True
            return Action.DEFECT

        return Action.COOPERATE


class TidemanAndChieruzzi(Agent):
    """
    Submitted to Axelrod's first tournament by Nicolas Tideman and Paula
    Chieruzzi.

    The description written in [Axelrod1980]_ is:
    > "This rule begins with cooperation and tit-for-tat. However, when the
    > other player finishes his second run of defections, an extra punishment is
    > instituted, and the number of punishing defections is increased by one with
    > each run of the other's defections. The other player is given a fresh start
    > if he is 10 or more points behind, if he has not just started a run of
    > defections, if it has been at least 20 moves since a fresh start, if there
    > are at least 10 moves remaining, and if the number of defections differs
    > from a 50-50 random generator by at least 3.0 standard deviations. A fresh
    > start involves two cooperations and then play as if the game had just
    > started. The program defects automatically on the last two moves."

    This is interpreted as:
    1. Every run of defections played by the opponent increases the number of
    defections that this strategy retaliates with by 1.

    2. The opponent is given a ‘fresh start’ if:
        - it is 10 points behind this strategy
        - and it has not just started a run of defections
        - and it has been at least 20 rounds since the last ‘fresh start’
        - and there are more than 10 rounds remaining in the match
        - and the total number of defections differs from a 50-50 random sample
          by at least 3.0 standard deviations.
        A ‘fresh start’ is a sequence of two cooperations followed by an assumption
        that the game has just started (everything is forgotten).

    3. The strategy defects on the last two moves.
    This strategy came 2nd in Axelrod’s original tournament.

    Names:
    - TidemanAndChieruzzi: [Axelrod1980]_
    """

    def __init__(self):
        super().__init__()

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        return Action.COOPERATE


class Nydegger(Agent):
    """
    Submitted to Axelrod's first tournament by Rudy Nydegger.

    The description written in [Axelrod1980]_ is:

    > "The program begins with tit-for-tat for the first three moves, except
    > that if it was the only one to cooperate on the first move and the only one
    > to defect on the second move, it defects on the third move. After the third
    > move, its choice is determined from the 3 preceding outcomes in the
    > following manner. Let A be the sum formed by counting the other's defection
    > as 2 points and one's own as 1 point, and giving weights of 16, 4, and 1 to
    > the preceding three moves in chronological order. The choice can be
    > described as defecting only when A equals 1, 6, 7, 17, 22, 23, 26, 29, 30,
    > 31, 33, 38, 39, 45, 49, 54, 55, 58, or 61. Thus if all three preceding moves
    > are mutual defection, A = 63 and the rule cooperates. This rule was
    > designed for use in laboratory experiments as a stooge which had a memory
    > and appeared to be trustworthy, potentially cooperative, but not gullible
    > (Nydegger, 1978)."
    """

    def __init__(self):
        super().__init__()
        self.A_to_defect = [
            1,
            6,
            7,
            17,
            22,
            23,
            26,
            29,
            30,
            31,
            33,
            38,
            39,
            45,
            49,
            54,
            55,
            58,
            61,
        ]
        self.score_map = {C: 0, D: 1}

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if not len(history):
            return C
        if len(history) == 1:
            return opp_history[0]
        if len(history) == 2:
            if opp_history[0] == D and opp_history[1] == C:
                return D
            return opp_history[1]
        A = (
            16 * self.score_map[history[-3]]
            + 32 * self.score_map[opp_history[-3]]
            + 4 * self.score_map[history[-2]]
            + 8 * self.score_map[opp_history[-2]]
            + 1 * self.score_map[history[-1]]
            + 2 * self.score_map[opp_history[-1]]
        )
        if A in self.A_to_defect:
            return D
        return C


class Grofman(Agent):
    """
    Submitted to Axelrod's first tournament by Bernard Grofman.
    The description written in [Axelrod1980]_ is:
    > "If the players did different things on the previous move, this rule
    > cooperates with probability 2/7. Otherwise this rule always cooperates."

    This strategy came 4th in Axelrod's original tournament.
    """

    def __init__(self):
        super().__init__()

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if not history:
            return C

        if history[-1] != opp_history[-1] and numpy.random.random() >= 2 / 7:
            return D
        return C
