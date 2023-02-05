from engine.components.types.unit_object import UnitObject
from engine.main_game import MainGame


class EndImage(UnitObject):

    def __init__(self):
        super().__init__('assets/images/end.jpg')

    def start(self, main_game: MainGame):
        super().start(main_game)
        self.position = (0, 0) # main_game.screen.location(left=0, top=0)
