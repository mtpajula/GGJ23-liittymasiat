from engine.components.scene import Scene
from lapland_defence.game_objects.game.info_text import InfoText
from lapland_defence.generators.poly_generator import PolyGenerator
from lapland_defence.generators.soldier_generator import SoldierGenerator


class GameScene(Scene):

    def __init__(self):
        super().__init__()
        self.objects: list = [
            InfoText()
        ]
        self.poly_generator = PolyGenerator('assets/lappi1milj_simple.geojson')
        self.soldier_generator = SoldierGenerator()
        self.enable_user_input = True

    def start(self, main_game):
        areas = self.poly_generator.generate(main_game.screen)
        self.soldier_generator.generate(areas=areas)
        self.objects.extend(areas)
        super().start(main_game)

    def draw(self, main_game):
        main_game.window.fill((0, 0, 0))
        super().draw(main_game)

    def on_event(self, main_game, position: tuple[int, int]):
        if self.enable_user_input:
            super().on_event(main_game, position)
        else:
            print('GameScene: User input disabled')
