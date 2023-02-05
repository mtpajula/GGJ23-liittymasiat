from engine.components.types.text_object import TextObject
from engine.main_game import MainGame


class RestartGame(TextObject):

    def __init__(self):
        super().__init__('Restart Game')
        self.heading = True

    def start(self, main_game: MainGame):
        super().start(main_game)
        self.position = main_game.screen.location(left=300, top=900)
        self.bounds = (500, 100)

    def draw(self, main_game):
        main_game.pygame.draw.rect(main_game.window, (0, 0, 0), (self.position[0]-32, self.position[1]-32, self.bounds[0], self.bounds[1]))
        super().draw(main_game)

    def on_bounds_event(self, main_game: MainGame):
        main_game.change_scene('intro')
