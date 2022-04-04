from datetime import datetime

import pandas as pd

from tournament.agents.axelrod_first import (
    Davis,
    Downing,
    Feld,
    Graaskamp,
    Grofman,
    Joss,
    Nydegger,
    Shubik,
    SteinAndRapoport,
    TidemanAndChieruzzi,
    Tullock,
)
from tournament.agents.random import RandomAgent
from tournament.agents.tft import TitForTat
from tournament.tournament import RoundRobinTournament


def main():
    agents = [
        TitForTat,
        TidemanAndChieruzzi,
        Nydegger,
        Grofman,
        Shubik,
        SteinAndRapoport,
        Davis,
        Graaskamp,
        Downing,
        Feld,
        Joss,
        Tullock,
        RandomAgent,
    ]

    tournament = RoundRobinTournament(agents)

    scores, times = tournament.play(
        continuation_probability=0.99654, repetitions=5000, jobs=12
    )

    data = [
        {
            "id": agent.__name__,
            "tn_score": sum(scores[agent]) / len(scores[agent]),
            "tn_time": sum(times[agent]) / len(times[agent]),
        }
        for agent in scores
    ]
    data.sort(key=lambda x: x["tn_score"], reverse=True)

    df = pd.DataFrame(data)
    df.to_csv(f"results/axelrod-1-{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.csv")


if __name__ == "__main__":
    main()
