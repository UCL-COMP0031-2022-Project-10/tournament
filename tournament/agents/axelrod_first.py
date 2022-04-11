from collections import Counter
from random import random
from typing import List, Optional, Tuple

import numpy.random
from numpy.random import RandomState
from scipy.stats import chisquare
from tournament.action import Action
from tournament.agent import Agent
from tournament.match import PAYOFF_MATRIX


class Davis(Agent):
    """
    This class implements the agent submitted by Morton Davis to Axelrod's first tournament.

    It is described by Axelrod as follows:
    > "A player starts by cooperating for 10 rounds then plays Grudger,
    > defecting if at any point the opponent has defected."

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_first.py#L28
    """

    def play_move(self, history: List[Action], opp_history: List[Action]):
        if len(history) < 10:
            return Action.COOPERATE

        if opp_history and Action.DEFECT in opp_history:
            return Action.DEFECT

        return Action.COOPERATE


class Graaskamp(Agent):
    """
    This class implements the agent submitted by James Graaskamp to Axelrod's first tournament.

    It is described by Axelrod as follows:
    > This rule plays tit-for-tat for 50 moves, defects on move 51, and then
    > plays 5 more moves of tit-for-tat. A check is then made to see if the player
    > seems to be RANDOM, in which case it defects from then on. A check is also
    > made to see if the other is TIT FOR TAT, ANALOGY (a program from the
    > preliminary tournament), and its own twin, in which case it plays tit-for-tat
    > Otherwise, it randomly defects every 5 to 15 moves, hoping that enough
    > trust has been built up so that the other player will not notice these
    > defections.

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_first.py#L656
    """

    def __init__(self, alpha: float = 0.05):
        """
        alpha: the significant level of p-value from chi-squared test.
        """
        super().__init__()

        self.alpha = alpha
        self.opponent_is_random = False
        self.opponent_is_identical = True
        self.opponent_is_tft = True
        self.next_random_defection_turn = None

        self.counts = {Action.COOPERATE: 0, Action.DEFECT: 0}

    def play_move(self, history: List[Action], opp_history: List[Action]):
        """
        Plays a move.
        """

        # Cooperate initially
        if not opp_history:
            return Action.COOPERATE

        self.counts[opp_history[-1]] += 1

        if history[-1] != opp_history[-1]:
            self.opponent_is_identical = False

        if len(history) > 1 and opp_history[-2] != history[-1]:
            self.opponent_is_tft = False

        # Play TFT in the first 56 turns
        if len(history) < 56:
            # Defect on the 51st turn
            if len(history) == 50:
                return Action.DEFECT

            # Play the opponent's last action
            return opp_history[-1]

        # Check if opponent is random
        p_value = chisquare(
            [self.counts[Action.COOPERATE], self.counts[Action.DEFECT]]
        ).pvalue
        self.opponent_is_random = (p_value >= self.alpha) or self.opponent_is_random

        # If so, defect for the rest of the game
        if self.opponent_is_random:
            return Action.DEFECT

        # Check if opponent is Tit For Tat or a clone of itself
        if self.opponent_is_tft or self.opponent_is_identical:
            # If so, play TFT
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
            return Action.DEFECT

        return Action.COOPERATE


class Shubik(Agent):
    """
    This class implements the agent submitted by Martin Shubik to Axelrod's first tournament.

    It is described by Axelrod as follows:
    > This rule cooperates until the other defects, and then defects once. If
    > the other defects again after the rule's cooperation is resumed, the rule
    > defects twice. In general, the length of retaliation is increased by one for
    > each departure from mutual cooperation. This rule is described with its
    > strategic implications in Shubik (1970). Further treatment of its is given
    > in Taylor (1976).

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_first.py#L656
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

    It is described by Axelrod as follows:
    > This rule plays tit-for-tat except that it cooperates on the first four
    > moves, it defects on the last two moves, and every fifteen moves it checks
    > to see if the opponent seems to be playing randomly. This check uses a
    > chi-squared test of the other's transition probabilities and also checks for
    > alternating moves of CD and DC.

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_first.py#L832

    """

    def __init__(self):
        super().__init__()

        self.alpha = 0.05
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
    This class implements the agent submitted by Nicolas Tideman and Paula Chieruzzi to Axelrod's first tournament.

    It is described by Axelrod as follows:
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

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_first.py#L906
    """

    def __init__(self):
        super().__init__()
        self.retaliation_length = 0
        self.retaliation_remaining = 0
        self.score_diff = 0
        self.fresh_start = False
        self.fresh_start_count = 0
        self.opp_D_count = 0

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        self.fresh_start_count += 1
        if not history:
            return Action.COOPERATE

        self.opp_D_count += opp_history[-1].value - 1  # C = 1, D = 2
        last_round = PAYOFF_MATRIX[(history[-1], opp_history[-1])]
        self.score_diff += last_round[0]
        self.score_diff -= last_round[1]

        if self.retaliation_remaining:
            self.retaliation_remaining -= 1
            return Action.DEFECT

        # if the other player has just started a run of defections
        if opp_history[-1] == Action.DEFECT:
            self.retaliation_remaining = self.retaliation_length
            self.retaliation_length += 1
            return Action.DEFECT

        # if the other player is 10 or more points behind
        # if it has been at least 20 moves since a fresh start
        if self.fresh_start_count >= 20 and self.score_diff >= 10:
            std_deviation = (len(opp_history) ** (1 / 2)) / 2
            lower = len(opp_history) / 2 - 3 * std_deviation
            upper = len(opp_history) / 2 + 3 * std_deviation
            if self.opp_D_count <= lower or self.opp_D_count >= upper:
                self.fresh_start = True

        if self.fresh_start:
            self.retaliation_length = 0
            self.fresh_start = False
            self.fresh_start_count = 0

        return Action.COOPERATE


class Nydegger(Agent):
    """
    This class implements the agent submitted by Rudy Nydegger to Axelrod's first tournament.

    It is described by Axelrod as follows:
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

    This implementation was adapted from the Axelrod library: https://github.com/Axelrod-Python/Axelrod/blob/00e18323c1b1af74df873773e44f31e1b9a299c6/axelrod/strategies/axelrod_first.py#L533
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
        self.score_map = {Action.COOPERATE: 0, Action.DEFECT: 1}

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if not history:
            return Action.COOPERATE

        if len(history) == 1:
            return opp_history[0]

        if len(history) == 2:
            if opp_history[0] == Action.DEFECT and opp_history[1] == Action.COOPERATE:
                return Action.DEFECT
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
            return Action.DEFECT

        return Action.COOPERATE


class Grofman(Agent):
    """
    This class implements the agent submitted by Bernard Grofman to Axelrod's first tournament.

    It is described by Axelrod as follows:
    > "If the players did different things on the previous move, this rule
    > cooperates with probability 2/7. Otherwise this rule always cooperates."
    """

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if not history:
            return Action.COOPERATE

        if history[-1] != opp_history[-1] and numpy.random.random() >= 2 / 7:
            return Action.DEFECT

        return Action.COOPERATE


class Tullock(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if len(history) <= 11:
            # always cooperate on first 11 moves.
            return Action.COOPERATE

        # 1) Calculate % of cooperate moves by opponent over the last 10 moves
        # 2) Tullock cooperates with probability (% of coop - 10). If % of coop < 0.1, defect.
        # % of cooperation moves by opp over the last 10 moves.
        percent_coop = opp_history[-10:].count(Action.COOPERATE) / 10
        if percent_coop <= 0.1:
            return Action.DEFECT

        if random() <= percent_coop - 10:
            return Action.COOPERATE
        return Action.DEFECT


class Downing(Agent):
    def __init__(self):
        # num of times opp has cooperated after Downing has cooperated.
        self._num_coop_following_coop = 0

        # num of times opp has cooperated after Downing has defected.
        self._num_coop_following_defect = 0
        self._num_defect = 0
        self._num_cooperate = 0

    def _calc_conditional_probs(self) -> Tuple[float, float]:
        alpha = self._num_coop_following_coop / (
            self._num_cooperate + 1
        )  # add 1 to remove divide by zero error. We assume in the nonexistent round 0, Downing cooperated.
        beta = self._num_coop_following_defect / self._num_defect

        return (alpha, beta)

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:

        # Calc P(C_o | C_s) = Prob(Opp cooperates | Downing cooperated previous turn) = alpha
        #      P(C_o | D_s) = Prob(Opp cooperates | Downing defected previous turn) = beta
        # R = reward (3), T = temptation (5), S = sucker (0), P = Punishment (1).
        # Expected Value for Cooperating (EV_C) = P(C_o | C_s) * R + (1 - P(C_o | C_s)) * S
        # Expected Value for Defecting (EV_D) = P(C_o | D_s) * T + (1 - P(C_o | D_s)) * P
        # If EV_C > EV_D => Cooperate. If EV_D > EV_C => Defect. If EV_D = EV_C, do opposite of last action that Downing executed.
        # Downing has pessimistic assumption that starting probabilities are 0.5 each. Consequently, Downing always defects on first two turns.

        if len(history) == 0:
            self._num_defect += 1
            return Action.DEFECT
        elif len(history) == 1:
            if opp_history[0] == Action.COOPERATE:
                self._num_coop_following_defect += 1
            self._num_defect += 1
            return Action.DEFECT

        if opp_history[-1] == Action.COOPERATE and history[-2] == Action.COOPERATE:
            self._num_coop_following_coop += 1
        if opp_history[-1] == Action.COOPERATE and history[-2] == Action.DEFECT:
            self._num_coop_following_defect += 1

        alpha, beta = self._calc_conditional_probs()
        ev_c = alpha * 3 + (1 - alpha) * 0
        ev_d = beta * 5 + (1 - beta) * 1
        if ev_c > ev_d:
            self._num_cooperate += 1
            return Action.COOPERATE
        elif ev_d > ev_c:
            self._num_defect += 1
            return Action.DEFECT
        if history[-1] == Action.DEFECT:
            self._num_cooperate += 1
            return Action.COOPERATE
        self._num_defect += 1
        return Action.DEFECT


class Joss(Agent):
    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:

        if not history:
            return Action.DEFECT

        if opp_history[-1] == Action.DEFECT:
            # always defect if opp defects
            return Action.DEFECT

        if random() <= 0.9:
            # if opp has cooperated, cooperate with 90% probability.
            return Action.COOPERATE
        return Action.DEFECT


class Feld(Agent):
    def __init__(self):
        self._rate_of_dec = 1 / 200  # rate at which _prob_coop decreases
        self._prob_coop = 1  # probability of cooperating after a cooperation by opp.

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if not history:
            return Action.COOPERATE

        if opp_history[-1] == Action.DEFECT:
            # always defect if opp defected.
            return Action.DEFECT

        if len(history) < 200:
            # over a period of 200 moves, linearly decrease prob to 0.5.
            self._prob_coop -= self._rate_of_dec

        if random() <= self._prob_coop:
            # cooperate with probability self._prob_coop else defect
            return Action.COOPERATE
        return Action.DEFECT


class Friedman(Agent):
    def __init__(self) -> None:
        super().__init__()

        self.defect = False

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        if not history:
            return Action.COOPERATE

        if opp_history[-1] == Action.DEFECT:
            self.defect = True

        return Action.DEFECT if self.defect else Action.COOPERATE
