from engine.components.scene import Scene
from lapland_defence import utils
from lapland_defence.game_objects.game.info_text import InfoText
from lapland_defence.game_objects.game.logo_image import LogoImage
from lapland_defence.game_objects.game.select_area_info import SelectAreaInfo
from lapland_defence.generators.poly_generator import PolyGenerator
from lapland_defence.generators.soldier_generator import SoldierGenerator
from lapland_defence.generators.soldier_types import FactionType


class GameScene(Scene):

    def __init__(self):
        super().__init__()
        self.objects: list = [
            LogoImage(),
            InfoText(),
            SelectAreaInfo()
        ]
        self.poly_generator = PolyGenerator('assets/lappi1milj_simple.geojson')
        self.soldier_generator = SoldierGenerator()
        self.enable_user_input = True
        self.areas = []

    def start(self, main_game):
        self.areas = self.poly_generator.generate(main_game.screen)
        self.soldier_generator.generate(areas=self.areas)
        self.objects.extend(self.areas)
        utils.soundManager.play_music('game')
        super().start(main_game)

    def draw(self, main_game):
        main_game.window.fill((0, 0, 0))
        super().draw(main_game)
        for area in self.areas:
            area.draw_soldiers(main_game)

    def on_event(self, main_game, position: tuple[int, int]):
        if self.enable_user_input:
            super().on_event(main_game, position)
        else:
            print('GameScene: User input disabled')

    def count_municipalities(self):
        player = 0
        p23g = 0
        scissors = 0

        for area in self.areas:
            if area.faction == FactionType.PLAYER:
                player += 1
            elif area.faction == FactionType.PLAYER:
                papers += 1
            elif area.faction == FactionType.PLAYER:
                scissors += 1
        return {
            FactionType.PLAYER: player,
            FactionType.P23G: player,
            FactionType.LOL: player,
            FactionType.PIRJO: player
        }