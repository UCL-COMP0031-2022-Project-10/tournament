import numpy as np
import pandas as pd

from tournament.action import Action
from tournament.agent import Agent
from tournament.agents.q_learning.tabular import TabularQLearner
from tournament.match import Match


class TabularAgent(TabularQLearner):
    def __init__(self) -> None:
        super().__init__()

        self.epsilon = 0.05
        self._lookback = 2
        self._discount_rate = 0.99
        self._learning_rate = 0.05
        self._evaluation_epsilon = 0.001
        self._epsilon_decay = 0.0
        self._decay_limit = 0.05


class ManualAgent(Agent):
    def play_move(self, history, opp_history):
        move = input("Move: ")
        if move == "C":
            return Action.COOPERATE
        elif move == "D":
            return Action.DEFECT
        elif move == "Q":
            raise RuntimeError()


tabular_agent = TabularAgent()
# tabular_agent._state = tabular_agent.get_initial_state()
tabular_agent.load("2022-04-07 03-48-14 - 39 - 449.3574193548387 - 31.npz")
#print(tabular_agent._q_table)
#print(tabular_agent._state)

manual_agent = ManualAgent()

match = Match(tabular_agent, manual_agent)

for i, ((move1, move2), (score1, score2), (reward1, reward2)) in enumerate(
    match.play_moves(continuation_probability=0.99654, limit=1000, noise=0)
):
    print(
        f"{i:<4} | \t {move1:<20} {score1:<8} {f'({reward1})':<20} {move2:<20} {score2:<8} {f'({reward2})':<10}"
    )
