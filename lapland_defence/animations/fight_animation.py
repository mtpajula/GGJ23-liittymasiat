from engine.components.types.animation import Animation


class FightAnimation(Animation):

    def __init__(self):
        super().__init__()
        self.time = 60
        self.counter = 0
        self.surfaces = {}
        self.current_surface = 0

    def start(self, main_game):
        super().start(main_game)
        self.surfaces[0] = main_game.pygame.image.load('assets/images/Smoke1.png')
        self.surfaces[20] = main_game.pygame.image.load('assets/images/Smoke2.png')
        self.surfaces[40] = main_game.pygame.image.load('assets/images/Smoke3.png')


    def draw(self, main_game) -> bool:
        if self.counter in self.surfaces:
            self.current_surface = self.counter

        main_game.window.blit(self.surfaces[self.current_surface], (main_game.target_area.position[0]-50, main_game.target_area.position[1]-50))

        self.counter += 1
        if self.counter > self.time:
            self.stop()

        return super().draw(main_game)
