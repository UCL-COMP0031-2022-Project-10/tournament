import numpy as np
import torch

from tournament.action import Action
from tournament.agents.agents import AGENTS
from tournament.environments.multiple import MultipleRuleBasedAgentEnvironment
from tournament.tournament import RoundRobinTournament


def train_and_evaluate(agents, cls, epochs=5000, tournament_agents=AGENTS, **kwargs):
    env = MultipleRuleBasedAgentEnvironment(agents, silent=True)
    agent = cls(**kwargs)
    env.train(
        trainee=agent,
        limit=200,
        epochs=epochs,
    )
    s = sum(env.counts.values())

    if hasattr(agent, "_q_network"):
        agent._q_network.eval()

    with torch.no_grad():
        tournament = RoundRobinTournament(tournament_agents, [agent])
        scores, times = tournament.play(
            continuation_probability=0.99654, repetitions=50, jobs=12
        )
        results = {agent: sum(scores[agent]) / len(scores[agent]) for agent in scores}

        return {
            "model": str(agent._q_network) if hasattr(agent, "_q_network") else None,
            **kwargs,
            "epochs": epochs,
            "tr_cooperation_percentage": env.counts[Action.COOPERATE] / s,
            "tr_defection_percentage": env.counts[Action.DEFECT] / s,
            "tr_final_loss": env.metric_history[-1],
            "tr_mean_reward": float(np.mean(env.rewards)),
            "tr_cumul_reward": float(np.sum(env.rewards)),
            "tr_cumul_regret": float(np.sum(3 - np.array(env.rewards))),
            "tn_rank": sorted(results, key=results.get, reverse=True).index(cls) + 1,
            "tn_mean_score": results[cls],
            "tn_mean_time": sum(times[cls]),
        }, agent


def evaluate(agents, cls, **kwargs):
    results, agent = train_and_evaluate(agents, cls, **kwargs)
    return results
