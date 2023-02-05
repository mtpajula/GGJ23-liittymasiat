from engine.components.scene import Scene
from lapland_defence import utils
from lapland_defence.game_objects.end.restart_game import RestartGame
from lapland_defence.game_objects.start.game_title import GameTitle
from lapland_defence.game_objects.start.start_image import StartImage


class EndScene(Scene):

    def __init__(self):
        super().__init__()
        self.objects: list = [
            StartImage(),
            RestartGame(),
            GameTitle(),
        ]

    def start(self, main_game):
        super().start(main_game)
        utils.soundManager.play_sound('intro')

    def draw(self, main_game):
        main_game.window.fill((0, 0, 0))
        super().draw(main_game)

    def close(self, main_game):
        utils.soundManager.sounds['intro'].stop()
        super().close(main_game)