from tournament.agents.randomAgent import RandomAgent
from tournament.agents.tft import TitForTat
from tournament.match import Match
from tournament.agents.axelrod_first import TidemanAndChieruzzi

match_length = 0
for (move1, move2), (score1, score2) in Match(TidemanAndChieruzzi(), RandomAgent()).play_moves(
    continuation_probability=0.99654, limit=1000, noise=0
):
    match_length += 1
    print(f"{move1:<20} {score1:<20} {move2:<20} {score2:<20}")

print(match_length)
