from enum import Enum


class SoldierType(Enum):
    ROCK = 1
    SCISSORS = 2
    PAPER = 3


class FactionType(Enum):
    PLAYER = 1
    P23G = 2
    PIRJO = 3
    LOL = 4


def get_faction_name(faction: FactionType) -> str:
    if faction == FactionType.PLAYER:
        return 'Laplanders'
    elif faction == FactionType.P23G:
        return '23G'
    elif faction == FactionType.LOL:
        return 'LOL'
    elif faction == FactionType.PIRJO:
        return 'PIRJO'
