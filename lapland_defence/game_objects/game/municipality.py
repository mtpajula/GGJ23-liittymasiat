from shapely import Polygon

from engine.components.types.area_object import AreaObject


class Municipality(AreaObject):

    def __init__(self, name, polygon: Polygon):
        super().__init__(name, polygon)

    def on_bounds_event(self, main_game):
        print(self.name)
        self.color = (255, 0, 0)
