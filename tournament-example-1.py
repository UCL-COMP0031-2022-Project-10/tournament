from tournament.agents.constant import AllC, AllD
from tournament.agents.random import Random
from tournament.agents.tft import TitForTat
from tournament.agents.JOSS import Joss
from tournament.agents.FELD import Feld
from tournament.agents.DOWNING import Downing
from tournament.agents.TULLOCK import Tullock
from tournament.tournament import RoundRobinTournament

if __name__ == "__main__":
    tournament = RoundRobinTournament([TitForTat, Random, AllC, AllD, Joss, Feld, Tullock, Downing])

    scores = tournament.play(
        continuation_probability=0.99654, repetitions=2000, jobs=12
    )

    print({agent: round(sum(scores[agent]) / len(scores[agent])) for agent in scores})
