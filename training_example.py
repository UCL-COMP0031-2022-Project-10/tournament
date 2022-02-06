from tournament.environments.single import MultipleRuleBasedAgentEnvironment
from tournament.agents.tabluar_q_learner import TabluarQLearner
from tournament.agents.random import RandomAgent

if __name__ == "__main__":
    environ = MultipleRuleBasedAgentEnvironment(RandomAgent)
    environ.train(TabluarQLearner())
