from engine.components.scene import Scene
from engine.main_game import MainGame
import cv2

from lapland_defence import utils

video = cv2.VideoCapture("assets/videos/intro_lapland.mp4")
success, video_image = video.read()
fps = video.get(cv2.CAP_PROP_FPS)


class IntroductionScene(Scene):

    def __init__(self):
        super().__init__()
        self.objects: list = [
        ]
        self.clock = None

    def start(self, main_game):
        super().start(main_game)
        self.clock = main_game.pygame.time.Clock()
        utils.soundManager.play_sound('intro')

    def draw(self, main_game):
        main_game.window.fill((0, 0, 0))
        self.clock.tick(fps)
        success, video_image = video.read()
        if success:
            video_surf = main_game.pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")

            main_game.window.blit(video_surf, (100, 0))
        else:
            print("no video")
            main_game.change_scene('game')

        super().draw(main_game)

    def close(self, main_game):
        utils.soundManager.sounds['intro'].stop()
        super().close(main_game)

    def on_event(self, main_game: MainGame, position: tuple[int, int]):
        super().on_event(main_game, position)

        main_game.change_scene('game')
