from typing import Dict, List, Optional, Tuple

from tournament.action import Action
from tournament.agent import Agent


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
