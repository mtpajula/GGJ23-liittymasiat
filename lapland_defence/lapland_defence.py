from engine.components.scene import Scene
from engine.main_game import MainGame
from lapland_defence.scenes.game_scene import GameScene
from lapland_defence.scenes.introduction_scene import IntroductionScene
from lapland_defence.scenes.start_scene import StartScene


class LaplandDefence(MainGame):

    def __init__(self):
        super().__init__(start_scene='start')
        self.scenes: dict[str, Scene] = {
            'start': StartScene(),
            'intro': IntroductionScene(),
            'game': GameScene()
        }
