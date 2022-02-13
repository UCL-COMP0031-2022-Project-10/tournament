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
