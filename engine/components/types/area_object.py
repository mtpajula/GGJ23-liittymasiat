from shapely import Polygon, Point

from engine.components.coordinates.screen import Screen
from engine.components.game_object import GameObject


class AreaObject(GameObject):

    def __init__(self, name, polygon: Polygon):
        super().__init__()
        self.name: str = name
        self.text_surface = None
        self.polygon: Polygon = polygon
        self.coords: list[tuple[int, int]] = []
        self.color = (0, 120, 0)

    def start(self, main_game):
        # self.text_surface = main_game.font.render(self.name, False, self.color)
        self.set_game_polygon(main_game.screen)
        self.position = (self.polygon.centroid.x, main_game.screen.height - self.polygon.centroid.y)

    def set_game_polygon(self, screen: Screen):
        # self.coords = [(100, 140), (120, 120), (130, 160), (120, 200), (110, 180)]
        for coord in self.polygon.exterior.coords:
            self.coords.append((coord[0], screen.height - coord[1]))

    def draw(self, main_game):
        main_game.pygame.draw.polygon(main_game.window, self.color, self.coords)
        # main_game.window.blit(self.text_surface, self.position)

    def on_bounds_event(self, main_game):
        pass

    def on_event(self, main_game, event_position: tuple[int, int]):
        tap_point = Point(event_position[0], main_game.screen.height - event_position[1])
        if tap_point.within(self.polygon):
            self.on_bounds_event(main_game)
