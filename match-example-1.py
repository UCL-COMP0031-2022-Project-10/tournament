from tournament.agents.axelrod_first import TidemanAndChieruzzi
from tournament.agents.random import RandomAgent
from tournament.agents.tft import TitForTat
from tournament.match import Match

print(
        f"%-4s | \t %-20s %-8s %-20s %-20s %-8s %-10s"%("turn","P1_action", "P1_score", "P1_reward", "P2_action", "P2_score", "P2_reward")
    )
for i, ((move1, move2), (score1, score2), (reward1, reward2)) in enumerate(
    Match(TidemanAndChieruzzi(), RandomAgent()).play_moves(
        continuation_probability=0.99654, limit=1000, noise=0
    )
):
    print(
        f"{i:<4} | \t {move1:<20} {score1:<8} {f'({reward1})':<20} {move2:<20} {score2:<8} {f'({reward2})':<10}"
    )
