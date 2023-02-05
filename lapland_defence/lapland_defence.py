from typing import Optional

from engine.components.scene import Scene
from engine.main_game import MainGame
from lapland_defence.game_objects.game.municipality import Municipality
from lapland_defence.scenes.game_scene import GameScene
from lapland_defence.scenes.introduction_scene import IntroductionScene
from lapland_defence.scenes.start_scene import StartScene
from lapland_defence.generators.soldier_types import FactionType



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

        # Area is already active
        if area.active:
            return

        # active are anot set -> select active area
        if self.active_area is None:
            # only player area can be set as active area
            if area.faction != FactionType.PLAYER:
                print('Prevent enemy area as active area')
                return
            print(f'set {area.name} to active')
            self.active_area = area
            self.active_area.set_active(self, True)
        else:
            if self.target_area is None:
                # Only non-player faction areas can be set as target
                if area.faction == FactionType.PLAYER:
                    print('Prevent player area as target')
                    return
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




