from engine.components.game_object import GameObject


class Scene:

    def __init__(self):
        self.objects: list[GameObject] = []

    def start(self, main_game):
        for game_object in self.objects:
            game_object.start(main_game)

    def draw(self, main_game):
        for game_object in self.objects:
            game_object.draw(main_game)

    def close(self, main_game):
        for game_object in self.objects:
            game_object.close(main_game)

    def on_event(self, main_game, position: tuple[int, int]):
        for game_object in self.objects:
            game_object.on_event(main_game, position)
