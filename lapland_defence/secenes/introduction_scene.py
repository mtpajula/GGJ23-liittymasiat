from engine.components.scene import Scene


class IntroductionScene(Scene):

    def __init__(self):
        super().__init__()
        self.objects: list = [
        ]

    def draw(self, main_game):
        main_game.window.fill((255, 255, 255))
        super().draw(main_game)

