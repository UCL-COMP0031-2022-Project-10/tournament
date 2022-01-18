from typing import List

from tournament.action import Action


class Agent:
    def __init__(self) -> None:
        pass

    def play_move(self, history: List[Action], opp_history: List[Action]) -> Action:
        """Plays a move.

        Args:
            history (List[Action]): The history of the agent's past moves.
            opp_history (List[Action]): The history of the agent's opponent's past moves.

        Raises:
            NotImplementedError: This is only a base class -- this method should be implemented by children.

        Returns:
            Action: The action to take (COOPERATE or DEFECT).
        """

        raise NotImplementedError()
