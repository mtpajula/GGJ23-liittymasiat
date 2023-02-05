from engine.components.game_object import GameObject
from lapland_defence.generators.soldier_types import SoldierType, FactionType
from lapland_defence.generators.textures import get_mini_soldier_texture


class AreaInfo(GameObject):

    def __init__(self):
        super().__init__()
        self.text_surface_info = None
        self.text_surface_player = None
        self.text_surface_p23g = None
        self.text_surface_lol = None
        self.text_surface_pirjo = None
        self.update: bool = True

    def start(self, main_game):
        self.position = main_game.screen.location(left=900, top=800)
        counts = main_game.game_scene.count_areas()
        self.text_surface_info = main_game.font.render(f'Areas in control', False, (255, 255, 255))
        self.text_surface_player = main_game.font.render(f'Laplanders: {counts[FactionType.PLAYER]}', False, (255, 255, 255))
        self.text_surface_p23g = main_game.font.render(f'23G: {counts[FactionType.P23G]}', False, (255, 255, 255))
        self.text_surface_lol = main_game.font.render(f'LOL: {counts[FactionType.LOL]}', False, (255, 255, 255))
        self.text_surface_pirjo = main_game.font.render(f'pirjo: {counts[FactionType.PIRJO]}', False, (255, 255, 255))

    def draw(self, main_game):
        if self.update:
            self.start(main_game)
            self.update = False
        main_game.window.blit(self.text_surface_info, (self.position[0], self.position[1]))
        main_game.window.blit(self.text_surface_player, (self.position[0], self.position[1] + 20))
        main_game.window.blit(self.text_surface_p23g, (self.position[0], self.position[1] + 40))
        main_game.window.blit(self.text_surface_lol, (self.position[0], self.position[1] + 60))
        main_game.window.blit(self.text_surface_pirjo, (self.position[0], self.position[1] + 80))

    def close(self, main_game):
        pass

    def on_event(self, main_game, event_position: tuple[int, int]):
        print("event")
        self.update = True
