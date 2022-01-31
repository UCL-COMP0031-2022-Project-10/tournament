from tournament.agents.axelrod_first import (
    Davis,
    Graaskamp,
    Grofman,
    Grudger,
    Nydegger,
    Shubik,
    SteinAndRapoport,
    TidemanAndChieruzzi,
)
from tournament.agents.axelrod_second import (
    Champion,
    Borufsen,
    Leyvraz,
    SecondByHarrington,
    SecondByWhiteK72R,
    SecondByBlackK83R,
    SecondByTidemanAndChieruzzi,
)
from tournament.agents.constant import AllC, AllD
from tournament.agents.Downing import Downing
from tournament.agents.Feld import Feld
from tournament.agents.Joss import Joss
from tournament.agents.pavlov import Pavlov
from tournament.agents.randomAgent import RandomAgent
from tournament.agents.tft import (
    TFTT,
    TTFT,
    GenerousTFT,
    GradualTFT,
    OmegaTFT,
    TitForTat,
)

AGENTS = [
    AllC,
    AllD,
    TitForTat,
    RandomAgent,
    Davis,
    Graaskamp,
    Shubik,
    SteinAndRapoport,
    Grudger,
    Nydegger,
    Grofman,
    Downing,
    Feld,
    Joss,
    Pavlov,
    OmegaTFT,
    TFTT,
    TTFT,
    GradualTFT,
    GenerousTFT,
    TidemanAndChieruzzi,
    Champion,
    Borufsen,
    Leyvraz,
    SecondByHarrington,
    SecondByWhiteK72R,
    SecondByBlackK83R,
    SecondByTidemanAndChieruzzi,
]