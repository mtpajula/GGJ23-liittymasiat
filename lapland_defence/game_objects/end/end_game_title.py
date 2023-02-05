from engine.components.types.text_object import TextObject
from engine.main_game import MainGame


class EndGameTitle(TextObject):

    def __init__(self):
        super().__init__('Lapland 2053 defense')
        self.heading = True

    def start(self, main_game: MainGame):
        super().start(main_game)
        self.position = main_game.screen.location(left=600, top=100)
