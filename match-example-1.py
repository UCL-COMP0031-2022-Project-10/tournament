from tournament.agents.random import Random
from tournament.agents.tft import TitForTat
from tournament.match import Match

for (move1, move2), (score1, score2) in Match(TitForTat(), Random()).play_moves(
    continuation_probability=0.99654, limit=1000, noise=0
):
    print(f"{move1:<20} {score1:<20} {move2:<20} {score2:<20}")
