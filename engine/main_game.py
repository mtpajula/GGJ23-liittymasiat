import pygame

from engine.components.coordinates.screen import Screen
from engine.components.scene import Scene
from engine.controllers.navigator import Navigator

# clock = pygame.time.Clock()


class MainGame:

    def __init__(self, start_scene: str):
        self.run: bool = True
        self.navigator: Navigator = Navigator(current_scene=start_scene)
        self.screen: Screen = Screen(width=1500, height=900)
        self.scenes: dict[str, Scene] = {}
        self.pygame = pygame
        self.window = None
        self.font = None

    def draw(self):
        """
        Draw current scene and its objects
        :return:
        """
        self.scenes[self.navigator.current_scene].draw(self)

    def handle_events(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.run = False

    def loop(self):
        while self.run:
            self.handle_events()
            # clock.tick(27)
            self.draw()
            self.pygame.display.flip()

    def start(self):
        self.pygame.init()
        self.window = self.pygame.display.set_mode((self.screen.width, self.screen.height))
        self.pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

        self.scenes[self.navigator.current_scene].start(self)

        self.loop()
        self.pygame.quit()

    def close(self):
        self.scenes[self.navigator.current_scene].close(self)
        self.run = False
