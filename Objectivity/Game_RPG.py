class Attributes:
    def __init__(self, attack, defence, life):
        self.attack = attack
        self.defence = defence
        self.life = life

class Character:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def attack(self, opponent):
        damage = max(0, self.attributes.attack - opponent.attributes.defence)
        opponent.attributes.life -= damage
        print(f"{self.name} atakuje {opponent.name} i zadaje {damage} obrażeń.")
        if opponent.attributes.life <= 0:
            print(f"{opponent.name} został pokonany!")

class Batman(Character):
    def __init__(self):
        attributes = Attributes(attack=10, defence=5, life=100)
        super().__init__("Batman", attributes)

class Joker(Character):
    def __init__(self):
        attributes = Attributes(attack=8, defence=3, life=80)
        super().__init__("Joker", attributes)


batman = Batman()
joker = Joker()

batman.attack(joker)
joker.attack(batman)
