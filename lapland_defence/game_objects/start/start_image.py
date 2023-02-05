from engine.components.types.unit_object import UnitObject
from engine.main_game import MainGame


class StartImage(UnitObject):

    def __init__(self):
        super().__init__('assets/images/start.jpg')

    def start(self, main_game: MainGame):
        super().start(main_game)
        self.position = main_game.screen.location(left=0, top=0)
