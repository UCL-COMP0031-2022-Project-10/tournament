from typing import Dict, List, Optional, Tuple

from tournament.action import Action
from tournament.agent import Agent

from scipy.stats import chisquare
from collections import Counter
from numpy.random import RandomState


class Davis(Agent):
    '''
    Submitted to Axelrod's first tournament by Morton Davis.

    The description written in [Axelrod1980]_ is:

    > "A player starts by cooperating for 10 rounds then plays Grudger,
    > defecting if at any point the opponent has defected."

    This strategy came 8th in Axelrod's original tournament.

    Names:

    - Davis: [Axelrod1980]_
    '''

    def __init__(self, rounds_to_cooperate: int = 10):
        '''
        rounds_to_cooperate: The number of rounds to play C.
        '''
        super().__init__()
        self._rounds_to_cooperate = rounds_to_cooperate

    def play_move(self, history: List[Action], opp_history: List[Action]):
        '''
        Begins by playing C, then plays D for the remaining rounds if the opponent ever plays D.
        '''
        if len(history) < self._rounds_to_cooperate:
            #print("Davis: playing C")
            return Action.COOPERATE
        if opp_history and Action.DEFECT in opp_history:
            #print("Davis: playing D")
            return Action.DEFECT
        #print("Davis: playing C")
        return Action.COOPERATE


class Graaskamp(Agent):
    """
    Submitted to Axelrod's first tournament by James Graaskamp.

    The description written in [Axelrod1980]_ is:

    > "This rule plays tit for tat for 50 moves, defects on move 51, and then
    > plays 5 more moves of tit for tat. A check is then made to see if the player
    > seems to be RANDOM, in which case it defects from then on. A check is also
    > made to see if the other is TIT FOR TAT, ANALOGY (a program from the
    > preliminary tournament), and its own twin, in which case it plays tit for
    > tat. Otherwise it randomly defects every 5 to 15 moves, hoping that enough
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
    Furthermore the test for the clone is implemented as checking that both
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
               #print("Graaskamp: playing D")
                return Action.DEFECT

            # Cooperate initially
            if not opp_history:
               #print("Graaskamp: playing C")
                return Action.COOPERATE

            # Play the opponent's last action
           #print("Graaskamp: playing " + str(opp_history[-1]))
            return opp_history[-1]

        cnt = Counter(opp_history)
        num_c = cnt[Action.COOPERATE]
        num_d = cnt[Action.DEFECT]

        # Check if opponent is random
        p_value = chisquare([num_c, num_d]).pvalue
        self.opponent_is_random = (
            p_value >= self.alpha
        ) or self.opponent_is_random

        # If so, defect for the rest of the game
        if self.opponent_is_random:
           #print("Graaskamp: playing D")
            return Action.DEFECT

        # Check if opponent is Tit For Tat or a clone of itself
        if (
            all(
                opp_history[i] == history[i - 1]
                for i in range(1, len(history))
            )
            or opp_history == history
        ):
            # If so, play TFT
           #print("Graaskamp: playing " + str(opp_history[-1]))
            return opp_history[-1]

        # Otherwise, randomly defect every 5 to 15 moves
        if self.next_random_defection_turn is None:
            self.next_random_defection_turn = RandomState().randint(5, 15) + len(history)

        if len(history) == self.next_random_defection_turn:
            self.next_random_defection_turn = RandomState().randint(5, 15) + len(history)
           #print("Graaskamp: playing D")
            return Action.DEFECT
        
       #print("Graaskamp: playing C")
        return Action.COOPERATE
