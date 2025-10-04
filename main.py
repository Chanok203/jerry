# Inheritance
# สืบทอด

# sub class, child class
# super class, parent class
# super() # get parent class
# override

class Character:
    def __init__(self, str, dex, int):
        self.str = str
        self.dex = dex
        self.int = int

    def attack(self):
        return sum([self.str, self.dex, self.int]) / 3

    def __str__(self):
        return "CHARACTER"


class Swordman(Character):
    def __init__(self):
        # Character.__init__(self, 20, 10, 0)
        super().__init__(20, 10, 0)
        self.give = 7

    # Override Method
    def attack(self):
        return (self.str * 2) + self.give

    def __str__(self):
        return "Swordman"


class Archer(Character):
    def __init__(self):
        super().__init__(10, 20, 0)

    def attack(self):
        return 2 * super().attack()

    def __str__(self):
        return "Archer"


class Wizard(Character):
    def __init__(self):
        super().__init__(5, 5, 25)

    def __str__(self):
        return "Wizard"


class Knight(Swordman):
    def __init__(self):
        super().__init__()
        self.give2 = 100

    def attack(self):
        # return Character.attack(self)
        return super(Swordman, self).attack()

swordman = Swordman()
archer = Archer()
wizard = Wizard()
knight = Knight()
character = Character(1, 1, 1)

character_list = [
    swordman,
    archer,
    wizard,
    character,
    knight,
]
for hero in character_list:
    print(hero, hero.attack())
