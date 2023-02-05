from engine.components.game_object import GameObject


class TextObject(GameObject):

    def __init__(self, text: str):
        super().__init__()
        self.text_surface = None
        self.text: str = text
        self.color = (255, 255, 255)
        self.heading = False

    def start(self, main_game):
        font = main_game.heading_font if self.heading else main_game.font
        self.text_surface = font.render(self.text, False, self.color)

    def draw(self, main_game):
        main_game.window.blit(self.text_surface, self.position)

    def close(self, main_game):
        pass

    def on_bounds_event(self, main_game):
        pass

    def on_event(self, main_game, event_position: tuple[int, int]):
        if self.position[0] <= event_position[0] <= (self.position[0] + self.bounds[0]) \
                and self.position[1] <= event_position[1] <= (self.position[1] + self.bounds[1]):
            self.on_bounds_event(main_game)
