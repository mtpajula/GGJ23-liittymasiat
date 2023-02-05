from engine.components.types.unit_object import UnitObject
from lapland_defence.generators.soldier_types import FactionType
from lapland_defence.generators.textures import get_faction_logo


class LogoImage(UnitObject):

    def __init__(self):
        super().__init__('assets/images/start.jpg')
        self.current_turn: FactionType = FactionType.PLAYER

    def start(self, main_game):
        self.texture = get_faction_logo(main_game.turn)
        super().start(main_game)
        self.position = main_game.screen.location(left=900, top=0)

    def draw(self, main_game):
        if self.current_turn != main_game.turn:
            self.start(main_game)
        super().draw(main_game)
