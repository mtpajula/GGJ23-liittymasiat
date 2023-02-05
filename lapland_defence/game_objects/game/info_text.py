from engine.components.types.text_object import TextObject

class InfoText(TextObject):

    def __init__(self):
        super().__init__('...')

    def start(self, main_game):
        self.text = f'Turn {main_game.turn}'
        super().start(main_game)
        self.position = main_game.screen.location(left=900, top=10)
        # self.bounds = (500, 100)


    def draw(self, main_game):
        self.text = f'Turn {main_game.turn}'
        super().draw(main_game)
