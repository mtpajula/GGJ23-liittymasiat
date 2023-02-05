from engine.components.scene import Scene
from lapland_defence import utils
from lapland_defence.game_objects.game.area_info import AreaInfo
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
            SelectAreaInfo(),
            AreaInfo()
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

    def on_game_event(self, main_game, position: tuple[int, int]):
        super().on_event(main_game, position)

    def count_areas(self):
        player = 0
        p23g = 0
        lol = 0
        pirjo = 0

        for area in self.areas:
            if area.faction == FactionType.PLAYER:
                player += 1
            elif area.faction == FactionType.P23G:
                p23g += 1
            elif area.faction == FactionType.LOL:
                lol += 1
            elif area.faction == FactionType.PIRJO:
                pirjo += 1
        return {
            FactionType.PLAYER: player,
            FactionType.P23G: p23g,
            FactionType.LOL: lol,
            FactionType.PIRJO: pirjo
        }