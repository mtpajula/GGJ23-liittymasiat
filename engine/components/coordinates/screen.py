

class Screen:

    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height

    def limits(self) -> int:
        return self.width if self.width < self.height else self.height

    def x(self, left: int) -> int:
        return int((self.limits() / 1000) * left)

    def y(self, top: int) -> int:
        return int((self.limits() / 1000) * top)

    def location(self, left: int, top: int) -> tuple[int, int]:
        return self.x(left), self.y(top)
