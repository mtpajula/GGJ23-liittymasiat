import pygame

from engine.components.coordinates.screen import Screen
from engine.components.scene import Scene


class MainGame:

    def __init__(self, start_scene: str):
        self.run: bool = True
        self.current_scene: str = start_scene
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
        self.scenes[self.current_scene].draw(self)

    def start_scene(self):
        self.scenes[self.current_scene].start(self)

    def handle_events(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.close()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self.scenes[self.current_scene].on_event(self, pos)

    def loop(self):
        while self.run:
            self.handle_events()
            # clock.tick(27)
            self.draw()
            self.pygame.display.flip()
        self.pygame.quit()

    def start(self):
        self.pygame.init()
        self.window = self.pygame.display.set_mode((self.screen.width, self.screen.height))
        self.pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

        self.start_scene()
        self.loop()

    def change_scene(self, scene: str):
        print(f'change scene to {scene}')
        self.current_scene = scene
        self.start_scene()

    def close(self):
        self.scenes[self.current_scene].close(self)
        self.run = False

