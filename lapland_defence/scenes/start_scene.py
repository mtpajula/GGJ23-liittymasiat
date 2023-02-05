from engine.components.scene import Scene
from lapland_defence import utils
from lapland_defence.game_objects.start.game_title import GameTitle
from lapland_defence.game_objects.start.start_game_text_object import StartGameTextButton
from lapland_defence.game_objects.start.start_image import StartImage


class StartScene(Scene):

    def __init__(self):
        super().__init__()
        self.objects: list = [
            StartImage(),
            StartGameTextButton(),
            GameTitle(),
        ]

    def start(self, main_game):
        super().start(main_game)
        utils.soundManager.play_sound('start')

    def close(self, main_game):
        utils.soundManager.sounds['start'].stop()
        super().close(main_game)