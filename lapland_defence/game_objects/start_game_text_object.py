from engine.components.types.text_object import TextObject
from engine.main_game import MainGame


class StartGameTextButton(TextObject):

    def __init__(self):
        super().__init__('Start Game')

    def start(self, main_game: MainGame):
        super().start(main_game)
        self.position = main_game.screen.location(left=500, top=500)
        self.bounds = (500, 100)

    def on_bounds_event(self, main_game: MainGame):
        print("change scene")
        main_game.navigator.current_scene = 'intro'
