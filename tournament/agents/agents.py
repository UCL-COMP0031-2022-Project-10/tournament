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
from tournament.agents.constant import AllC, AllD
from tournament.agents.Downing import Downing
from tournament.agents.Feld import Feld
from tournament.agents.Joss import Joss
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

AGENTS = [
    AllC,
    AllD,
    TitForTat,
    Random,
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
]
