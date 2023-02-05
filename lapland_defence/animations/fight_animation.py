from engine.components.types.animation import Animation


class FightAnimation(Animation):

    def __init__(self):
        super().__init__()
        self.time = 50
        self.counter = 0

    def start(self, main_game):
        super().start(main_game)

    def draw(self, main_game) -> bool:
        self.counter += 1
        if self.counter > self.time:
            self.stop()

        return super().draw(main_game)
