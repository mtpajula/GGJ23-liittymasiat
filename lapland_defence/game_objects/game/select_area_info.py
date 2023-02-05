from engine.components.game_object import GameObject
from lapland_defence.generators.soldier_types import SoldierType
from lapland_defence.generators.textures import get_mini_soldier_texture


class SelectAreaInfo(GameObject):

    def __init__(self):
        super().__init__()
        self.text_surface_info = None
        self.text_surface_rock = None
        self.text_surface_paper = None
        self.text_surface_scissors = None
        self.image_surface_rock = None
        self.image_surface_paper = None
        self.image_surface_scissors = None
        self.update: bool = True

    def start(self, main_game):
        self.position = main_game.screen.location(left=900, top=350)
        if main_game.active_area is not None:
            counts = main_game.active_area.count_soldiers()
            self.text_surface_info = main_game.font.render(f'Units in {main_game.active_area.name}', False, (255, 255, 255))
            self.text_surface_rock = main_game.font.render(f'{counts[SoldierType.ROCK]}', False, (255, 255, 255))
            self.text_surface_paper = main_game.font.render(f'{counts[SoldierType.PAPER]}', False, (255, 255, 255))
            self.text_surface_scissors = main_game.font.render(f'{counts[SoldierType.SCISSORS]}', False, (255, 255, 255))

            self.image_surface_rock = main_game.pygame.image.load(
                get_mini_soldier_texture(soldier_type=SoldierType.ROCK, faction=main_game.active_area.faction)
            )
            self.image_surface_paper = main_game.pygame.image.load(
                get_mini_soldier_texture(soldier_type=SoldierType.PAPER, faction=main_game.active_area.faction)
            )
            self.image_surface_scissors = main_game.pygame.image.load(
                get_mini_soldier_texture(soldier_type=SoldierType.SCISSORS, faction=main_game.active_area.faction)
            )

    def draw(self, main_game):
        if main_game.active_area is not None:
            if self.update:
                self.start(main_game)
                self.update = False
            main_game.window.blit(self.text_surface_info, (self.position[0], self.position[1]))
            main_game.window.blit(self.text_surface_rock, (self.position[0]+20, self.position[1] + 20))
            main_game.window.blit(self.text_surface_paper, (self.position[0]+20, self.position[1] + 40))
            main_game.window.blit(self.text_surface_scissors, (self.position[0]+20, self.position[1] + 60))

            main_game.window.blit(self.image_surface_rock, (self.position[0], self.position[1] + 20))
            main_game.window.blit(self.image_surface_paper, (self.position[0], self.position[1] + 40))
            main_game.window.blit(self.image_surface_scissors, (self.position[0], self.position[1] + 60))

    def close(self, main_game):
        pass

    def on_event(self, main_game, event_position: tuple[int, int]):
        self.update = True
