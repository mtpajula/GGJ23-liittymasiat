from engine.components.types.text_object import TextObject
from engine.main_game import MainGame


class GameTitle(TextObject):

    def __init__(self):
        super().__init__('Lapland 2053 defense')
        self.heading = True

    def start(self, main_game: MainGame):
        super().start(main_game)
        self.position = main_game.screen.location(left=300, top=200)
