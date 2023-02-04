

class Screen:

    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height

    def limits(self):
        return self.width if self.width < self.height else self.height
