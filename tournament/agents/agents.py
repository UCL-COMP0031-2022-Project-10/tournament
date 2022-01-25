from tournament.agents.axelrod_first import (
    Davis,
    Graaskamp,
    Grofman,
    Grudger,
    Nydegger,
    Shubik,
    SteinAndRapoport,
)
from tournament.agents.constant import AllC, AllD
from tournament.agents.downing import Downing
from tournament.agents.feld import Feld
from tournament.agents.joss import Joss
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
]
