import itertools

grid = {
    "p_cc": [0.25, 0.5, 0.75, 1],
    "p_cd": [0.25, 0.5, 0.75, 1],
    "p_dc": [0.25, 0.5, 0.75, 1],
    "p_dd": [0.25, 0.5, 0.75, 1],
}

H = {
    i: dict(zip(grid.keys(), hyperparameters))
    for i, hyperparameters in enumerate(itertools.product(*grid.values()))
}

print("from tournament.action import Action")
print("from tournament.agents.random import ProbabilisticLB2")
print()

for i, h in H.items():
    print(
        "class Stoc"
        + str(i)
        + """(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): """
        + str(h["p_cc"])
        + ", (Action.COOPERATE, Action.DEFECT): "
        + str(h["p_cd"])
        + ", (Action.DEFECT, Action.COOPERATE): "
        + str(h["p_dc"])
        + ", (Action.DEFECT, Action.DEFECT): "
        + str(h["p_dd"])
        + " }\n\n"
    )

print()
print()

print("STOC_AGENTS = [", ",".join([f"Stoc{i}" for i in H]) + "]\n\n")

print("STOC_HYPERPARAMS =", {f"Stoc{i}": h for i, h in H.items()})
