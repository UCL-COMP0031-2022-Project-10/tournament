from tournament.agents.q_learning.dqn import LargeLookback
from tournament.agents.tft import TitForTat
from tournament.environments.single import SingleRuleBasedAgentEnvironment

env = SingleRuleBasedAgentEnvironment(TitForTat)

agent = LargeLookback()

env.train(
    trainee=agent,
    continuation_probability=0.99,
    limit=10000,
    noise=0,
    repetitions=100,
    epochs=10,
)

print(agent._q_network)
print(env.counts)
