import random

from lapland_defence.game_objects.game.municipality import Municipality
from lapland_defence.game_objects.game.soldier import Soldier
from lapland_defence.generators.soldier_types import SoldierType, FactionType


class SoldierGenerator:

    def get_random_type(self, faction: FactionType) -> Soldier:
        s_type = random.choice(list(SoldierType))
        return Soldier(soldier_type=s_type, faction=faction)

    def generate_into_municipality(self, municipality: Municipality):
        for i in range(0, random.randint(0, 9)):
            soldier = self.get_random_type(municipality.faction)
            municipality.soldiers.append(soldier)

    def generate(self, areas: list):
        for area in areas:
            self.generate_into_municipality(area)
