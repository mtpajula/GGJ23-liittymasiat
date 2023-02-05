

class Animation:

    def __init__(self,):
        self.run = False

    def start(self, main_game):
        self.run = True

    def draw(self, main_game) -> bool:
        return self.run

    def stop(self):
        self.run = False
