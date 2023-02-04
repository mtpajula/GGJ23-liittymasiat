from engine.components.game_object import GameObject


class UnitObject(GameObject):

    def __init__(self, texture: str):
        super().__init__()
        self.texture: str = texture
        self.surface = None

    def start(self, main_game):
        self.surface = main_game.pygame.image.load(self.texture)

    def draw(self, main_game):
        main_game.window.blit(self.surface, self.position)
