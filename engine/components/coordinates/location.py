from engine.components.coordinates.screen import Screen


class Location:

    def __init__(self, x: int, y: int, screen: Screen):
        self.x: int = x
        self.y: int = y
        self.screen: Screen = screen

    def relative_x(self):
        return (self.screen.limits() / 1000)
