class Warrior:
    def __init__(self, attack=5, health=50, defense=0, vampirism=0, heal_power=0):
        self.attack = 5
        self.health = 50
        self.max_health = self.health
        self.defense = 0
        self.vampirism = 0
        self.heal_power = 0

        self.is_alive = True
        self.range_attack = False
        self.do_heal = False
        self.has_vampirism = False
        self.has_defense = False

    def __str__(self):
        return 'Warrior'
        # return f'Warrior {self.attack} {self.health} {self.defense} {self.vampirism} {self.heal_power}'

    def __repr__(self):
        return 'Warrior'

    def equip_weapon(self, weapon_name):
        self.max_health += weapon_name.health
        self.health += weapon_name.health
        if self.max_health <= 0:
            self.max_health = 0
            self.is_alive = 0
        self.attack += weapon_name.attack
        if self.attack <= 0:
            self.attack = 0
        if self.has_defense:
            self.defense += weapon_name.defense
            if self.defense <= 0:
                self.defense = 0
        if self.has_vampirism:
            self.vampirism += weapon_name.vampirism
            if self.vampirism <= 0:
                self.vampirism = 0
        if self.do_heal:
            self.heal_power += weapon_name.heal_power
            if self.heal_power <= 0:
                self.heal_power = 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7
        self.max_health = self.health

    def __str__(self):
        # return f'Knight {self.attack} {self.health} {self.defense} {self.vampirism} {self.heal_power}'
        return 'Knight'

    def __repr__(self):
        return 'Knight'


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.defense = 2
        self.attack = 3
        self.has_defense = True
        self.max_health = self.health

    def __str__(self):
        # return f'Defender {self.attack} {self.health} {self.defense} {self.vampirism} {self.heal_power}'
        return 'Defender'

    def __repr__(self):
        return 'Defender'


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.vampirism = 50
        self.health = 40
        self.attack = 4
        self.has_vampirism = True
        self.max_health = self.health

    def __str__(self):
        # return f'Vampire {self.attack} {self.health} {self.defense} {self.vampirism} {self.heal_power}'
        return 'Vampire'

    def __repr__(self):
        return 'Vampire'


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.range_attack = True
        self.max_health = self.health

    def __str__(self):
        # return f'Lancer {self.attack} {self.health} {self.defense} {self.vampirism} {self.heal_power}'
        return 'Lancer'

    def __repr__(self):
        return 'Lancer'


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 0
        self.health = 60
        self.heal_power = 2
        self.do_heal = True
        self.max_health = self.health

    def heal(self, unit):
        unit.health += self.heal_power
        if unit.health > unit.max_health:
            unit.health = unit.max_health

    def __str__(self):
        return 'Healer'
        # return f'Healer {self.attack} {self.health} {self.defense} {self.vampirism} {self.heal_power}'

    def __repr__(self):
        return 'Healer'


class Warlord(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.attack = 4
        self.defense = 2
        self.max_health = self.health
        self.has_defense = True

    def __str__(self):
        return 'Warlord'
        # return f'Warlord {self.attack} {self.health} {self.defense} {self.vampirism} {self.heal_power}'

    def __repr__(self):
        return 'Warlord'


class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1


# Weapons
# =======================
class Weapon:
    def __init__(self, health=0, attack=0, defense=0, vampirism=0, heal_power=0):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power


class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.health = 5
        self.attack = 2


class Shield(Weapon):
    def __init__(self):
        super().__init__()
        self.health = 20
        self.attack = -1
        self.defense = 2


class GreatAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.health = -15
        self.attack = 5
        self.defense = -2
        self.vampirism = 10


class Katana(Weapon):
    def __init__(self):
        super().__init__()
        self.health = -20
        self.attack = 6
        self.defense = -5
        self.vampirism = 50


class MagicWand(Weapon):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.attack = 3
        self.heal_power = 3


# =======================

def fight(unit_1, unit_2):
    flag = 'First'
    while unit_1.is_alive and unit_2.is_alive:
        if flag == 'First':
            damage = unit_2.defense - unit_1.attack
            if damage < 0:
                unit_2.health = unit_2.health + damage
                unit_1.health -= __import__('math').floor(damage * unit_1.vampirism / 100)
            flag = 'Second'

        else:
            damage = unit_1.defense - unit_2.attack
            if damage < 0:
                unit_1.health = unit_1.health + damage
                unit_2.health -= __import__('math').floor(damage * unit_2.vampirism / 100)
            flag = 'First'

        if unit_1.health <= 0:
            unit_1.is_alive = False
        if unit_2.health <= 0:
            unit_2.is_alive = False

    return unit_1.is_alive


class Army(list):

    def __init__(self, arr=None):
        super().__init__()
        if arr is None:
            arr = []
        self.units = arr

    def add_units(self, Warrior, count):
        if isinstance(Warrior(), Warlord):
            count = 1
        for i in range(count):
            self.append(Warrior())
        self.units = self

    def hp(self):
        return list(map(lambda x: (x, x.health), self.units))

    def move_units(self):
        if any(isinstance(x, Warlord) for x in self.units):

            # move lancers
            for unit in range(len(self.units)):
                if any(isinstance(x, Warlord) for x in self.units):
                    if isinstance(self.units[unit], Lancer):
                        self.units.insert(0, self.units.pop(unit))
                    elif not any(isinstance(x, Lancer) for x in self.units) and not isinstance(self.units[unit],
                                                                                               Warlord) and not isinstance(
                            self.units[unit], Healer):
                        self.units.insert(0, self.units.pop(unit))
                        break

            # move healers
            for unit in range(len(self.units)):
                if isinstance(self.units[unit], Healer):
                    self.units.insert(1, self.units.pop(unit))

            # move warlord
            for unit in range(len(self.units)):
                if isinstance(self.units[unit], Warlord):
                    self.units.append(self.units.pop(unit))
                    break


class Battle:

    def fight(self, unit_1, unit_2):
        while len(unit_1.units) and len(unit_2.units):

            flag = 'First'
            while unit_1.units and unit_2.units:
                if flag == 'First':
                    damage = unit_2.units[0].defense - unit_1.units[0].attack
                    if damage < 0:
                        unit_2.units[0].health = unit_2.units[0].health + damage
                        unit_1.units[0].health -= damage * unit_1.units[0].vampirism / 100

                    # Heal
                    for unit in range(len(unit_1.units) - 1):
                        if len(unit_1.units) > 1 and unit_1.units[unit + 1].do_heal:
                            unit_1.units[unit + 1].heal(unit_1.units[unit])

                    # Lancer attack
                    if unit_1.units[0].range_attack and len(unit_2.units) > 1:
                        damage_to_behind = (unit_2.units[1].defense - unit_1.units[0].attack) * 0.5
                        if damage_to_behind < 0:
                            unit_2.units[1].health = unit_2.units[1].health + damage_to_behind
                            unit_1.units[0].health -= damage_to_behind * unit_1.units[0].vampirism / 100

                    flag = 'Second'

                else:
                    damage = unit_1.units[0].defense - unit_2.units[0].attack
                    if damage < 0:
                        unit_1.units[0].health = unit_1.units[0].health + damage
                        unit_2.units[0].health -= damage * unit_2.units[0].vampirism / 100

                    # Heal
                    for unit in range(len(unit_2.units) - 1):
                        if len(unit_2.units) > 1 and unit_2.units[unit + 1].do_heal:
                            unit_2.units[unit + 1].heal(unit_2.units[unit])

                    # Lancer attack
                    if unit_2.units[0].range_attack and len(unit_1.units) > 1:
                        damage_to_behind = (unit_1.units[1].defense - unit_2.units[0].attack) * 0.5
                        if damage_to_behind < 0:
                            unit_1.units[1].health = unit_1.units[1].health + damage_to_behind
                            unit_2.units[0].health -= damage_to_behind * unit_2.units[0].vampirism / 100

                    flag = 'First'

                if unit_1.units[0].health <= 0:
                    unit_1.units.pop(0)
                    unit_1.move_units()
                if len(unit_2.units) > 1 and unit_2.units[1].health <= 0:
                    unit_2.units.pop(1)
                    unit_2.move_units()
                if len(unit_1.units) > 1 and unit_1.units[1].health <= 0:
                    unit_1.units.pop(1)
                    unit_1.move_units()

                if unit_2.units[0].health <= 0:
                    unit_2.units.pop(0)
                    unit_2.move_units()
                    flag = 'First'

                # print('1', unit_1.hp())
                # print('2', unit_2.hp())
            return bool(unit_1.units)

    def straight_fight(self, unit_1, unit_2):
        while unit_1.units and unit_2.units:
            unit_1.move_units()
            unit_2.move_units()
            biggest_army, mini_army = sorted([unit_1.units, unit_2.units], key=len, reverse=True)
            for i in range(len(mini_army)):
                fight(unit_1.units[i], unit_2.units[i])
            unit_1 = Army(list(filter(lambda x: x.is_alive, unit_1.units)))
            unit_2 = Army(list(filter(lambda x: x.is_alive, unit_2.units)))
        return bool(unit_1.units)

if __name__ == '__main__':
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 2)
    army_1.add_units(Lancer, 3)
    army_1.add_units(Defender, 1)
    army_1.add_units(Warlord, 1)
    army_2.add_units(Warlord, 5)
    army_2.add_units(Vampire, 1)
    army_2.add_units(Rookie, 1)
    army_2.add_units(Knight, 1)
    army_1.units[0].equip_weapon(Sword())
    army_2.units[0].equip_weapon(Shield())
    army_1.move_units()
    army_2.move_units()
    battle = Battle()
    assert battle.straight_fight(army_1, army_2) == False
