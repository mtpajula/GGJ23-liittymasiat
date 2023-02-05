from engine.components.scene import Scene
from lapland_defence import utils
from lapland_defence.game_objects.end.credits import Credits
from lapland_defence.game_objects.end.end_game_title import EndGameTitle
from lapland_defence.game_objects.end.end_image import EndImage
from lapland_defence.game_objects.end.restart_game import RestartGame
from lapland_defence.game_objects.end.winner_text import WinnerText



class EndScene(Scene):

    def __init__(self):
        super().__init__()
        self.objects: list = [
            EndImage(),
            RestartGame(),
            EndGameTitle(),
            Credits(),
            WinnerText()
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