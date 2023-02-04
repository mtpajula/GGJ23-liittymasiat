from engine.components.scene import Scene
from lapland_defence.generators.poly_generator import PolyGenerator


class GameScene(Scene):

    def __init__(self):
        super().__init__()
        self.objects: list = []
        self.poly_generator = PolyGenerator('assets/lappi1milj.geojson')

    def start(self, main_game):
        self.objects.extend(self.poly_generator.generate(main_game.screen))
        super().start(main_game)

    def draw(self, main_game):
        main_game.window.fill((0, 0, 0))
        super().draw(main_game)
