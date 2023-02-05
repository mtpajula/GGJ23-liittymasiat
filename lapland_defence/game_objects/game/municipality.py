from shapely import Polygon

from engine.components.types.area_object import AreaObject
from lapland_defence.game_objects.game.soldier import Soldier
from lapland_defence.generators.soldier_types import FactionType


class Municipality(AreaObject):

    def __init__(self, name, polygon: Polygon, faction: FactionType):
        super().__init__(name, polygon)
        self.active = False
        self.target = False
        self.color = (0, 120, 0)
        self.soldiers: list[Soldier] = []
        self.faction: FactionType = faction

    def set_color(self):
        if self.faction == FactionType.PLAYER:
            self.color = (100, 150, 0)
        if self.faction == FactionType.P23G:
            self.color = (0, 100, 0)
        if self.faction == FactionType.LOL:
            self.color = (0, 120, 100)
        if self.faction == FactionType.PIRJO:
            self.color = (100, 100, 0)

        if self.active:
            self.color = (255, 0, 0)

        if self.target:
            self.color = (0, 255, 0)

    def start(self, main_game):
        self.set_color()
        super().start(main_game)

        for soldier in self.soldiers:
            soldier.start(main_game)

    def draw(self, main_game):
        super().draw(main_game)

    def draw_soldiers(self, main_game):
        for i, soldier in enumerate(self.soldiers):
            soldier.position = (self.position[0] + i * 5, self.position[1] + i * 5)
            soldier.draw(main_game)

    def set_active(self, main_game, value: bool):
        self.active = value
        self.set_color()
        self.draw(main_game)

    def set_target(self, main_game, value: bool):
        self.target = value
        self.set_color()
        self.draw(main_game)

    def on_bounds_event(self, main_game):
        main_game.select_area(self)
        # print(f'{self.name} color to {self.color}')
