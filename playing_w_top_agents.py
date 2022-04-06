import pandas as pd
import numpy as np
from tournament.agents.q_learning.tabular import TabularQLearner
from tournament.action import Action


rank1_agent = TabularQLearner()
rank1_agent._lookback = 2
rank1_agent.setup()
rank1_agent.load("models/2022-03-27 07-17-32 (798.4580645161291).npz")
print(rank1_agent._q_table)

agent_history = []
my_history = []
while 1:
    move = input("Move: ")
    if move == "C":
        agent_move = rank1_agent.play_move(agent_history, my_history)
        my_history.append(Action.COOPERATE)
        agent_history.append(agent_move)
        print(f"Agent played {agent_move}")
    elif move == "D":
        agent_move = rank1_agent.play_move(agent_history, my_history)
        my_history.append(Action.DEFECT)
        agent_history.append(agent_move)
        print(f"Agent played {agent_move}")
    elif move == "Q":
        break
    
        
    
