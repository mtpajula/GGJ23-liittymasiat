from lapland_defence.game_objects.game.municipality import Municipality
from lapland_defence.generators.soldier_generator import SoldierGenerator
from lapland_defence.generators.soldier_types import SoldierType


class FightLogic:

    def fight(self, attacker: Municipality, defender: Municipality) -> bool:

        win_points = 0

        attacker_soldiers = attacker.count_soldiers()
        defender_soldiers = defender.count_soldiers()
        win_points += attacker_soldiers[SoldierType.ROCK] - defender_soldiers[SoldierType.PAPER]
        win_points += attacker_soldiers[SoldierType.PAPER] - defender_soldiers[SoldierType.SCISSORS]
        win_points += attacker_soldiers[SoldierType.SCISSORS] - defender_soldiers[SoldierType.ROCK]

        if win_points > 0:
            defender.faction = attacker.faction
            # SoldierGenerator().generate_into_municipality(municipality=defender)
            defender.soldiers = attacker.soldiers.copy()
            attacker.soldiers = attacker.soldiers[:1]
            if len(defender.soldiers) > 1:
                defender.soldiers = defender.soldiers[:-1]
            if len(defender.soldiers) > 2:
                defender.soldiers = defender.soldiers[:-2]

            for soldier in defender.soldiers:
                soldier.faction = attacker.faction

            # attacker.soldiers = [SoldierGenerator().get_random_type(faction=attacker.faction)]
            return True

        if len(attacker.soldiers) > 1:
            attacker.soldiers = attacker.soldiers[:-1]

        if len(defender.soldiers) > 1:
            defender.soldiers = defender.soldiers[:-1]

        return False

    def move(self, attacker: Municipality, defender: Municipality):

        defender.soldiers = attacker.soldiers.copy()
        defender.soldiers.extend(attacker.soldiers.copy())

        if len(attacker.soldiers) > 1:
            attacker.soldiers = attacker.soldiers[:1]

        if len(defender.soldiers) > 1:
            defender.soldiers = defender.soldiers[:-1]

        print("move troops")
        pass

