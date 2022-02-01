from typing import List, Tuple

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


class TrainableAgent(Agent):
    """
    An interface for trainable agents.
    """

    def setup(self):
        """Prepares a trainable agent for training and gameplay."""
        pass

    def notify_prematch(self):
        """Handles new match starts in training."""
        pass

    def notify_postmatch(self):
        """Handles match endings in training."""
        pass

    def teardown(self):
        """Tears down a trainable again following training or gameplay."""
        pass

    def update(self, moves: Tuple[Action, Action], scores: Tuple[float, float]):
        raise NotImplementedError()
