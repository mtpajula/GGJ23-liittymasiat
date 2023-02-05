from lapland_defence.generators.soldier_types import SoldierType, FactionType


def get_soldier_texture(soldier_type: SoldierType, faction: FactionType) -> str:
    return 'assets/test.png'


def get_faction_logo(faction: FactionType) -> str:
    if faction == FactionType.PLAYER:
        return 'assets/images/logo_player.png'
    elif faction == FactionType.P23G:
        return 'assets/images/logo_23g.png'
    elif faction == FactionType.LOL:
        return 'assets/images/Logo_lol.png'
    elif faction == FactionType.PIRJO:
        return 'assets/images/logo_pirjo.png'
