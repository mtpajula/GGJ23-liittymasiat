from engine.components.types.text_object import TextObject
from lapland_defence.generators.soldier_types import get_faction_name


class WinnerText(TextObject):

    def __init__(self):
        super().__init__('')
        self.heading = True

    def start(self, main_game):
        self.text = f'{get_faction_name(main_game.winner())} won'
        super().start(main_game)
        self.position = main_game.screen.location(left=800, top=200)
