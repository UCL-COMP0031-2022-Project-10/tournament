from tournament.agents.tabluar_q_learner import TabluarQLearner
from tournament.agents.tft import TitForTat
from tournament.environments.single import SingleRuleBasedAgentEnvironment

env = SingleRuleBasedAgentEnvironment(TitForTat)

agent = TabluarQLearner()

env.train(
    trainee=agent,
    continuation_probability=1,
    limit=10000,
    noise=0,
    repetitions=1,
    epochs=1,
)


print(f"{'Trainee move':<20} {'TFT move':<20}")
for ((move1, move2),), (value1, value2) in agent._q_table.items():
    print(f"{move1:<20} {move2:<20} => {round(value1, 4):<10} {round(value2, 4):<10}")
# print(f"{'Trainee move':<20} {'TFT move':<20}")
# for ((move1, move2),), (value1, value2) in agent._q_table.items():
#     print(f"{move1:<20} {move2:<20} => {round(value1, 4):<10} {round(value2, 4):<10}")
