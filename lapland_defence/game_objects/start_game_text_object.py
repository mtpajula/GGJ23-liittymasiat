from engine.components.game_object import GameObject
from engine.main_game import MainGame


class StartGameTextButton(GameObject):

    def __init__(self):
        self.text_surface = None

    def draw(self, main_game: MainGame):
        main_game.window.blit(self.text_surface, (100, 100))

    def close(self, main_game: MainGame):
        pass

    def start(self, main_game: MainGame):
        self.text_surface = main_game.font.render('Some Text', False, (255, 255, 255))
