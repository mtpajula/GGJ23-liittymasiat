from engine.components.types.text_object import TextObject
from lapland_defence.generators.soldier_types import FactionType, get_faction_name


class InfoText(TextObject):

    def __init__(self):
        super().__init__('...')
        self.current_turn: FactionType = FactionType.PLAYER

    def start(self, main_game):
        self.current_turn = main_game.turn
        self.text = f'In turn: {get_faction_name(self.current_turn)}'
        super().start(main_game)
        self.position = main_game.screen.location(left=900, top=300)
        # self.bounds = (500, 100)

    def draw(self, main_game):
        if self.current_turn != main_game.turn:
            self.start(main_game)
        super().draw(main_game)
