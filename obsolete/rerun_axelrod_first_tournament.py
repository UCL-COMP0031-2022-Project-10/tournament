from tournament.agents.agents import (
    Davis,
    Downing,
    Feld,
    Graaskamp,
    Grofman,
    Grudger,
    Joss,
    Nydegger,
    Shubik,
    SteinAndRapoport,
    TidemanAndChieruzzi,
    Tullock,
    TitForTat,
    RandomAgent,
)
from tournament.tournament import RoundRobinTournament

"""
Axelrod First Tournament

Round robin tournament 

14 players

200 moves

5 repetitions
"""
agents = [
    Davis,
    Downing,
    Feld,
    Graaskamp,
    Grofman,
    Grudger,
    Joss,
    Nydegger,
    Shubik,
    SteinAndRapoport,
    TidemanAndChieruzzi,
    Tullock,
    TitForTat,
    RandomAgent,
]
if __name__ == "__main__":
    tournament = RoundRobinTournament(agents)

    scores, times = tournament.play(limit=200, repetitions=5, jobs=4)

    results = [
        (agent, round(sum(scores[agent]) / len(scores[agent])), sum(times[agent]))
        for agent in scores
    ]
    results.sort(key=lambda x: x[1], reverse=True)

    for c, score, time in results:
        print(f"{c.__name__:<30} {score:<20} {time:<20}")
