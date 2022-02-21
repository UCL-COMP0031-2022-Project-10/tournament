import numpy as np

from tournament.agents.q_learning.tabular import DoubleLookback, TripleLookback
from tournament.agents.tft import TitForTat
from tournament.environments.single import SingleRuleBasedAgentEnvironment

env = SingleRuleBasedAgentEnvironment(TitForTat)

agent = TripleLookback()

env.train(
    trainee=agent,
    continuation_probability=1,
    limit=10000,
    noise=0,
    repetitions=100,
    epochs=1,
)


print(np.round_(agent._q_table, decimals=0))


# for moves, (value1, value2) in agent._q_table.items():
#     print(
#         f"{str(moves):<100} => {round(value1, 4):<10} {round(value2, 4):<10} {'DEFECTS' if value1 < value2 else 'COOPERATES'}"
#     )
