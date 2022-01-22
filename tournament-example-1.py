from tournament.agents.constant import AllC, AllD
from tournament.agents.random import Random
from tournament.agents.tft import TitForTat, OmegaTFT, TFTT, TTFT, GradualTFT, GenerousTFT
from tournament.agents.pavlov import Pavlov
from tournament.tournament import RoundRobinTournament
from tournament.agents.axelrod_first import Davis, Graaskamp


if __name__ == "__main__":
    tournament = RoundRobinTournament([TitForTat, Random, AllC, AllD, Davis, Graaskamp, OmegaTFT, Pavlov, TFTT, TTFT, GradualTFT, GenerousTFT])

    scores = tournament.play(
        continuation_probability=0.99654, repetitions=50, jobs=12
    )

    unsorted_result = {agent: round(sum(scores[agent]) / len(scores[agent])) for agent in scores}
    sorted_result = sorted(unsorted_result.items(), key=lambda x:x[1])
    #print(unsorted_result)
    #print(sorted_result)
    for i in sorted_result:
        print(i)
