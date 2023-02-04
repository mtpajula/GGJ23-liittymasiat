

class Screen:

    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height

    def limits(self) -> int:
        return self.width if self.width < self.height else self.height

    def diff(self) -> int:
        return abs(self.width - self.height)

    def x_shift(self) -> int:
        return int(self.diff() / 2) if self.width > self.height else 0

    def y_shift(self) -> int:
        return int(self.diff() / 2) if self.width < self.height else 0

    def x(self, left: int) -> int:
        return int((self.limits() / 1000) * left) + self.x_shift()

    def y(self, top: int) -> int:
        return int((self.limits() / 1000) * top) + self.y_shift()

    def location(self, left: int, top: int) -> tuple[int, int]:
        return self.x(left), self.y(top)

    def change(self, x_y: tuple[int, int]) -> tuple[int, int]:
        return self.location(left=x_y[0], top=x_y[1])

