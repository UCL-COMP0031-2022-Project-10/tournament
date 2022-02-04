from tournament.agents.axelrod_first import TidemanAndChieruzzi
from tournament.agents.random import RandomAgent
from tournament.agents.tft import TitForTat
from tournament.match import Match

for i, ((move1, move2), (score1, score2), (reward1, reward2)) in enumerate(
    Match(TidemanAndChieruzzi(), RandomAgent()).play_moves(
        continuation_probability=0.99654, limit=1000, noise=0
    )
):
    print(
        f"{i:<4} | \t {move1:<20} {score1:<8} {f'({reward1})':<20} {move2:<20} {score2:<8} {f'({reward2})':<10}"
    )
