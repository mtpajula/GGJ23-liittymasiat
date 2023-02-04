from engine.components.scene import Scene
from engine.main_game import MainGame


class IntroductionScene(Scene):

    def __init__(self):
        super().__init__()
        self.objects: list = [
        ]

    def draw(self, main_game):
        main_game.window.fill((255, 255, 255))
        super().draw(main_game)

    def on_event(self, main_game: MainGame, position: tuple[int, int]):
        super().on_event(main_game, position)
        main_game.change_scene('game')
