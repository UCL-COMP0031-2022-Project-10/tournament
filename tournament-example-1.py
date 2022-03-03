from tournament.agents.agents import AGENTS
from tournament.tournament import RoundRobinTournament

if __name__ == "__main__":
    tournament = RoundRobinTournament(AGENTS)

    scores, times = tournament.play(
        continuation_probability=0.99654, repetitions=20, jobs=12
    )

    results = [
        (agent, round(sum(scores[agent]) / len(scores[agent])), sum(times[agent]))
        for agent in scores
    ]
    results.sort(key=lambda x: x[1], reverse=True)

    for c, score, time in results:
        print(f"{c.__name__:<30} {score:<20} {time:<20}")
