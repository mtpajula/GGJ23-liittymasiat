from engine.components.types.area_object import AreaObject
from engine.main_game import MainGame


class AreaTap:

    def on_tap(self, main_game: MainGame, area: AreaObject):
        print(area.name)
        area.color = (255, 0, 0)
