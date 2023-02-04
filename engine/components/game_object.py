
class GameObject:

    def __init__(self):
        self.bounds: tuple[int, int] = (100, 100)
        self.position: tuple[int, int] = (0, 0)

    def start(self, main_game):
        pass

    def draw(self, main_game):
        pass

    def close(self, main_game):
        pass

    def on_event(self, main_game, event_position: tuple[int, int]):
        pass
