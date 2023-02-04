from typing import Optional

from engine.components.scene import Scene
from engine.main_game import MainGame
from lapland_defence.game_objects.game.municipality import Municipality
from lapland_defence.scenes.game_scene import GameScene
from lapland_defence.scenes.introduction_scene import IntroductionScene
from lapland_defence.scenes.start_scene import StartScene


class LaplandDefence(MainGame):

    def __init__(self):
        super().__init__(start_scene='game')
        self.scenes: dict[str, Scene] = {
            'start': StartScene(),
            'intro': IntroductionScene(),
            'game': GameScene()
        }
        self.active_area: Optional[Municipality] = None
        self.target_area: Optional[Municipality] = None

    def select_area(self, area: Municipality):

        if area.active:
            return

        if self.active_area is None:
            print(f'set {area.name} to active')
            self.active_area = area
            self.active_area.set_active(self, True)
        else:
            if self.target_area is None:
                if area.polygon.distance(self.active_area.polygon) < 0.1:
                    print(f'set {area.name} to target')
                    self.target_area = area
                    self.target_area.set_target(self, True)
                    self.attack()
            else:
                print(f'clear all areas')
                self.active_area.set_active(self, False)
                self.target_area.set_target(self, False)
                self.target_area.target = False
                self.active_area = None
                self.target_area = None

    def attack(self):
        print('attack!')




