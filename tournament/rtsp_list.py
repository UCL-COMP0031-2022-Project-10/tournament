from typing import List
from tournament.action import Action


# rtsp list (reward/temptation/sucker/punishment list)
# input: histories of an agent and its opponent, respectively 
# return: list of results
#               0 for mutual cooperation, 1 for temptation profit,
#               2 for sucker's deflict  , 3 for mutual punishment.
def rtsp_list(history: List[Action], opp_history: List[Action]) -> List[int]:
    return_list = []
    for i in range(len(history)):
        if history[i] == Action.COOPERATE and opp_history[i] == Action.COOPERATE:
            return_list.append(0)
        elif history[i] == Action.DEFECT and opp_history[i] == Action.COOPERATE:
            return_list.append(1)
        elif history[i] == Action.COOPERATE and opp_history[i] == Action.DEFECT:
            return_list.append(2)
        else:  # if(history[i] == Action.COOPERATE and opp_history[i] == Action.COOPERATE)
            return_list.append(3)
    return return_list
