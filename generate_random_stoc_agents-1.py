import itertools
from random import random

H = {
    i: {
        "p_c": random(),
        "p_d": random(),
    }
    for i in range(100)
}

print("from tournament.action import Action")
print("from tournament.agents.random import ProbabilisticLB1")
print()

for i, h in H.items():
    print(
        "class Stoc"
        + str(i)
        + """(ProbabilisticLB1):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE,): """
        + str(h["p_c"])
        + ", (Action.DEFECT,): "
        + str(h["p_d"])
        + " }\n\n"
    )

print()
print()

print("STOC_AGENTS = [", ",".join([f"Stoc{i}" for i in H]) + "]\n\n")

print("STOC_HYPERPARAMS =", {f"Stoc{i}": h for i, h in H.items()})
