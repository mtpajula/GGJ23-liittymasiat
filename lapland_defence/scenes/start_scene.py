from engine.components.scene import Scene
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
