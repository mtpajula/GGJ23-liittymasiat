from engine.components.scene import Scene
from lapland_defence.game_objects.start_game_text_object import StartGameTextButton


class StartScene(Scene):

    def __init__(self):
        super().__init__()
        self.objects: list = [
            StartGameTextButton()
        ]