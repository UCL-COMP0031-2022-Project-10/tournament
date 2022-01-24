from tournament.agents.axelrod_first import (
    Davis,
    Graaskamp,
    Grudger,
    Shubik,
    SteinAndRapoport,
)
from tournament.agents.constant import AllC, AllD
from tournament.agents.pavlov import Pavlov
from tournament.agents.random import Random
from tournament.agents.tft import (
    TFTT,
    TTFT,
    GenerousTFT,
    GradualTFT,
    OmegaTFT,
    TitForTat,
)
from tournament.tournament import RoundRobinTournament

if __name__ == "__main__":
    tournament = RoundRobinTournament(
        [
            TitForTat,
            Random,
            AllC,
            AllD,
            Davis,
            Graaskamp,
            Shubik,
            SteinAndRapoport,
            Grudger,
            OmegaTFT,
            Pavlov,
            TFTT,
            TTFT,
            GradualTFT,
            GenerousTFT,
        ]
    )

    scores = tournament.play(
        continuation_probability=0.99654, repetitions=1000, jobs=12
    )

    unsorted_result = {
        agent: round(sum(scores[agent]) / len(scores[agent])) for agent in scores
    }
    sorted_result = sorted(unsorted_result.items(), key=lambda x: x[1], reverse=True)
    for c, score in sorted_result:
        print(c.__name__, score)
