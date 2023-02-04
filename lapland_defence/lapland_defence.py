from engine.components.scene import Scene
from engine.main_game import MainGame
from lapland_defence.secenes.introduction_scene import IntroductionScene
from lapland_defence.secenes.start_scene import StartScene


class LaplandDefence(MainGame):

    def __init__(self):
        super().__init__(start_scene='start')
        self.scenes: dict[str, Scene] = {
            'start': StartScene(),
            'intro': IntroductionScene()
        }
