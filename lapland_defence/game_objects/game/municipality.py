from shapely import Polygon

from engine.components.types.area_object import AreaObject
from lapland_defence.game_objects.game.soldier import Soldier
from lapland_defence.generators.soldier_types import FactionType, SoldierType


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
            self.color = (220, 94, 242)
        if self.faction == FactionType.LOL:
            self.color = (37, 51, 128)
        if self.faction == FactionType.PIRJO:
            self.color = (117, 23, 122)

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
        rocks = 0
        papers = 0
        scissors = 0
        for i, soldier in enumerate(self.soldiers):
            if soldier.type == SoldierType.ROCK:
                soldier.position = (self.position[0]-40, self.position[1] - rocks * 5)
                rocks += 1
            elif soldier.type == SoldierType.PAPER:
                soldier.position = (self.position[0]-20, self.position[1] - papers * 5)
                papers += 1
            elif soldier.type == SoldierType.SCISSORS:
                soldier.position = (self.position[0], self.position[1] - scissors * 5)
                scissors += 1
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

    def count_soldiers(self) -> dict:
        rocks = 0
        papers = 0
        scissors = 0
        for soldier in self.soldiers:
            if soldier.type == SoldierType.ROCK:
                rocks += 1
            elif soldier.type == SoldierType.PAPER:
                papers += 1
            elif soldier.type == SoldierType.SCISSORS:
                scissors += 1
        return {
            SoldierType.ROCK: rocks,
            SoldierType.PAPER: papers,
            SoldierType.SCISSORS: scissors,
        }