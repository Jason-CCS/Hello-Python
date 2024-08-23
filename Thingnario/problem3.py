import random


class Character:
    def introduce(self):
        pass

    def attack(self, opponent: 'Character', attack_func):
        pass

    def defend(self, attack_point):
        pass


class Fighter(Character):
    def __int__(self):
        pass

    def __init__(self, name, life_point, magic_point, attack_point, defense_point):
        self.name = name
        self.life_point = life_point
        self.magic_point = magic_point
        self.attack_point = attack_point
        self.defense_point = defense_point

    def introduce(self):
        print(f"Hi, {self.name} here!")

    def attack(self, opponent: 'Fighter', attack_func):
        print(f"{self.name} attacks {opponent.name}.")
        attack_point = attack_func(self.attack_point)
        print(f"attack_point is {attack_point}")
        opponent.defend(attack_point)

    def defend(self, attack_point):
        damage = max(0, attack_point - self.defense_point)
        self.life_point -= damage
        print(f"{self.name} got damage points {damage} points! {self.name}'s life point now is {self.life_point}.")


# We can rewrite Swordsman to avoid repeating arguments in Fighter type.
class VarArgsSwordsman(Fighter):
    def __init__(self, *args, **kwargs):
        if len(args) != 5:
            raise ValueError("Exactly 5 arguments are expected")
        super().__init__(*args)
        super().introduce()
        self.weapon = kwargs.get("weapon", "Normal Sword")
        self.equipment = kwargs.get("equipment", "Leather")

    def attack(self, opponent: Fighter, attack_func):
        print(f"{self.name} uses {self.weapon} to attack.")
        super().attack(opponent, attack_func)

    def defend(self, attack_point):
        print(f"{self.name} uses {self.equipment} to defend.")
        super().defend(attack_point)

# Decorator Design Pattern
class Decorator(Character):
    def __init__(self, fighter: Fighter):
        self.fighter = fighter

    def introduce(self):
        self.fighter.introduce()

    def attack(self, opponent: Fighter, attack_func):
        self.fighter.attack(opponent, attack_func)

    def defend(self, attack_point):
        self.fighter.defend(attack_point)


class StrongDecorator(Decorator):
    def __init__(self, fighter):
        super().__init__(fighter)

    def attack(self, opponent: Fighter, attack_func):
        # Double attack points before attack and restore them after attack
        self.fighter.attack_point *= 2
        try:
            self.fighter.attack(opponent, attack_func)
        finally:
            self.fighter.attack_point /= 2

    def defend(self, attack_point):
        # Double defense points during defense and restore them after defense
        self.fighter.defense_point *= 2
        try:
            self.fighter.defend(attack_point)
        finally:
            self.fighter.defense_point /= 2


# write a demo code here. We have two swordsmen, and they give each other one attack.
foo = VarArgsSwordsman("Foo", 100, 50, 8, 2, weapon="Normal Sword", equipment="Leather")
bar = VarArgsSwordsman("Bar", 100, 35, 12, 5, weapon="Dark Sword", equipment="Armor")
if_power_attack = lambda point: point * (2 if random.randint(0, 100) > 80 else 1)
foo.attack(bar, if_power_attack)
bar.attack(foo, if_power_attack)

print(f"{foo.name} used magic point 25 and became strong!!!")
foo.magic_point -= 25
foo.name = "Strong Foo"
strong_foo = StrongDecorator(foo)
strong_foo.attack(bar, if_power_attack)
bar.attack(foo, if_power_attack)



