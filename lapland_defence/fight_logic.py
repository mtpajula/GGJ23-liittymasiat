from lapland_defence.game_objects.game.municipality import Municipality


class FightLogic:

    def fight(self, attacker: Municipality, defender: Municipality) -> bool:
        if len(attacker.soldiers) >= len(defender.soldiers):
            defender.faction = attacker.faction
            defender.soldiers = attacker.soldiers.copy()
            for soldier in defender.soldiers:
                soldier.faction = attacker.faction
            attacker.soldiers = attacker.soldiers[:1]
            return True
        return False

