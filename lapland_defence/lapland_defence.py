from typing import Optional, cast

from engine.components.scene import Scene
from engine.main_game import MainGame
from lapland_defence.animations.fight_animation import FightAnimation
from lapland_defence.fight_logic import FightLogic
from lapland_defence.game_objects.game.municipality import Municipality
from lapland_defence.scenes.end_scene import EndScene
from lapland_defence.scenes.game_scene import GameScene
from lapland_defence.scenes.introduction_scene import IntroductionScene
from lapland_defence.scenes.start_scene import StartScene
from lapland_defence.generators.soldier_types import FactionType
from engine.soundmanager import SoundManager
import lapland_defence.utils as utils



class LaplandDefence(MainGame):

    def __init__(self):
        super().__init__(start_scene='game')
        self.scenes: dict[str, Scene] = {
            'start': StartScene(),
            'intro': IntroductionScene(),
            'game': GameScene(),
            'end': EndScene()
        }
        self.game_scene: GameScene = cast(GameScene, self.scenes['game'])
        self.active_area: Optional[Municipality] = None
        self.target_area: Optional[Municipality] = None

        # initialize sound manager
        utils.soundManager = SoundManager()

        # TODO: Failed loading libvorbisfile-3.dll: The specified module could not be found.
        # utils.soundManager.play_music('carnival')

        self.turn: FactionType = FactionType.PLAYER
        self.active_animation = None
        self.fight_logic: FightLogic = FightLogic()

        self.pygame.display.set_caption('Lapland 2053 defence')

        self.lost_factions = []

    def select_area(self, area: Municipality):

        # Area is already active
        if area.active:
            self.active_area.set_active(self, False)
            self.active_area = None
            return

        # active are anot set -> select active area
        if self.active_area is None:
            # only player area can be set as active area
            if area.faction != self.turn:
                # print('Prevent enemy area as active area')
                return
            # print(f'set {area.name} to active')
            self.active_area = area
            self.active_area.set_active(self, True)
            utils.soundManager.play_sound('select')
        else:
            if self.target_area is None:
                # Only non-player faction areas can be set as target
                if area.faction == self.turn:
                    # print('Prevent player area as target')
                    return
                if area.polygon.distance(self.active_area.polygon) < 0.1:
                    # print(f'set {area.name} to target')
                    self.target_area = area
                    self.target_area.set_target(self, True)
                    self.attack()
            else:
                # print(f'clear all areas')
                self.active_area.set_active(self, False)
                self.target_area.set_target(self, False)
                self.target_area.target = False
                self.active_area = None
                self.target_area = None

    def attack(self):
        print('attack!')
        utils.soundManager.play_sound('attack')
        self.active_animation = FightAnimation()
        self.active_animation.start(self)

    def draw(self):
        super().draw()
        if self.active_animation is None:
            self.game_scene.enable_user_input = True
        else:
            self.game_scene.enable_user_input = False
            animation_running = self.active_animation.draw(self)
            if not animation_running:
                self.active_animation = None
                self.solve_fight()

                if self.game_over():
                    self.change_scene('end')

    def solve_fight(self):
        self.fight_logic.fight(attacker=self.active_area, defender=self.target_area)
        self.active_area.set_active(self, False)
        self.target_area.set_target(self, False)
        self.target_area.target = False
        self.active_area = None
        self.target_area = None

        self.find_losers()

        self.change_faction()
        self.game_scene.on_game_event(self, (0, 0))

    def find_losers(self):
        area_count = self.game_scene.count_areas()
        if area_count[FactionType.PLAYER] == 0 and FactionType.PLAYER not in self.lost_factions:
            self.lost_factions.append(FactionType.PLAYER)
        if area_count[FactionType.PIRJO] == 0 and FactionType.PIRJO not in self.lost_factions:
            self.lost_factions.append(FactionType.PIRJO)
        if area_count[FactionType.P23G] == 0 and FactionType.P23G not in self.lost_factions:
            self.lost_factions.append(FactionType.P23G)
        if area_count[FactionType.LOL] == 0 and FactionType.LOL not in self.lost_factions:
            self.lost_factions.append(FactionType.LOL)

    def game_over(self) -> bool:
        return len(self.lost_factions) == 3

    def change_faction(self):
        if self.turn == FactionType.PLAYER:
            self.turn = FactionType.P23G
            if self.turn not in self.lost_factions:
                return

        if self.turn == FactionType.P23G:
            self.turn = FactionType.LOL
            if self.turn not in self.lost_factions:
                return

        if self.turn == FactionType.LOL:
            self.turn = FactionType.PIRJO
            if self.turn not in self.lost_factions:
                return

        if self.turn == FactionType.PIRJO:
            self.turn = FactionType.PLAYER
            if self.turn not in self.lost_factions:
                return

        print(self.turn)