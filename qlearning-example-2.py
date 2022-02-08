from tournament.agents.random import RandomAgent
from tournament.agents.tabluar_q_learner import TabluarQLearner
from tournament.agents.tabluar_q_learners import TDoubleLookBack, TTripleLookBack
from tournament.environments.single import SingleRuleBasedAgentEnvironment

env = SingleRuleBasedAgentEnvironment(RandomAgent)

agent = TDoubleLookBack()

env.train(
    trainee=agent,
    continuation_probability=1,
    limit=500000,
    noise=0,
    repetitions=1,
    epochs=1,
)


for moves, (value1, value2) in agent._q_table.items():
    print(
        f"{str(moves):<100} => {round(value1, 4):<10} {round(value2, 4):<10} {'DEFECTS' if value1 < value2 else 'COOPERATES'}"
    )
