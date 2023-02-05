from engine.components.game_object import GameObject
from engine.main_game import MainGame


class Credits(GameObject):

    def __init__(self):
        super().__init__()
        self.texts = [
            "Credits",
            "",
            "Mikko P - Game Design / Programming",
            "sokuni - Game Design / Music / Voice acting",
            "Siiri P - Game Design / Art",
            "AI / Stable diffusion 2.1 - Intro art",
            "",
            "Special thanks:",
            "",
            "Pettis - Additional programming / retro sound FX",
            "",
            "The game music uses the sample:",
            "Sandyrb Tubular Bells 02",
            " -> TUBULAR 007.wav @ Freesounds.org",
            "The original sample has been transposed to E",
            "and slightly cut from the end."
        ]
        self.surfaces = []

    def start(self, main_game: MainGame):
        super().start(main_game)
        self.position = main_game.screen.location(left=600, top=300)
        self.surfaces = []
        for text in self.texts:
            self.surfaces.append(main_game.font.render(text, False, (255, 255, 255)))

    def draw(self, main_game: MainGame):
        super().draw(main_game)
        for i, surface in enumerate(self.surfaces):
            main_game.window.blit(surface, (self.position[0], self.position[1] + i*20))
