
import random 
from action import Action
print(random.random())
history = [Action.COOPERATE,Action.COOPERATE,Action.COOPERATE,Action.COOPERATE,Action.COOPERATE]
opp_history = [Action.DEFECT,Action.DEFECT,Action.DEFECT,Action.DEFECT,Action.DEFECT]
if len(opp_history) < 5:
    print("COOPERATE")
opp_defection_count_l5 = 0
for i in range(5):
    opp_defection_count_l5 += 1 if(opp_history[-5:][i] == Action.DEFECT) else 0
prob_coop = {0: 1.0, 1: 1.0, 2: 0.88, 3: 0.68, 4: 0.4, 5: 0.04}
if random.random() <= prob_coop[opp_defection_count_l5]:
    print("COOPERATE")
else:
    print("Action.DEFECT")