from engine.components.scene import Scene
from lapland_defence.generators.poly_generator import PolyGenerator
from lapland_defence.generators.soldier_generator import SoldierGenerator


class GameScene(Scene):

    def __init__(self):
        super().__init__()
        # self.objects: list = []
        self.poly_generator = PolyGenerator('assets/lappi1milj_simple.geojson')
        self.soldier_generator = SoldierGenerator()

    def start(self, main_game):
        areas = self.poly_generator.generate(main_game.screen)
        self.soldier_generator.generate(areas=areas)
        self.objects.extend(areas)
        super().start(main_game)

    def draw(self, main_game):
        main_game.window.fill((0, 0, 0))
        super().draw(main_game)
