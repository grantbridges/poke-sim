class Pokemon:
    def __init__(self, max_hp, attack, defense, sp_attack, sp_defense, speed):
        # basic stats
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed

class Charmander(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, 39, 52, 43, 60, 50, 65)

class Squirtle(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, 44, 48, 65, 50, 64, 43)