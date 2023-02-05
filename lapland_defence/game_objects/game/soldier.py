
from engine.components.types.unit_object import UnitObject
from lapland_defence.generators.soldier_types import SoldierType, FactionType
from lapland_defence.generators.textures import get_soldier_texture, get_mini_soldier_texture


class Soldier(UnitObject):

    def __init__(self, soldier_type: SoldierType, faction: FactionType):
        self.type: SoldierType = soldier_type
        self.faction: FactionType = faction
        super().__init__(texture=get_mini_soldier_texture(soldier_type=self.type, faction=self.faction))

