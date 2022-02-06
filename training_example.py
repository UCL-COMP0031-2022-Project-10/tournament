from tournament.environments.single import MultipleRuleBasedAgentEnvironment
from tournament.agents.tabluar_q_learner import TabluarQLearner
from tournament.agents.random import RandomAgent
from tournament.agents.tft import TitForTat

if __name__ == "__main__":
    environ = MultipleRuleBasedAgentEnvironment(TitForTat)
    environ.train(TabluarQLearner())
