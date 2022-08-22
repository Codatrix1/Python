class User(object):
    def sign_in(self):
        return "User logged in !!"


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return f"Attacking with the power of {self.power}"


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        return f"Number of arrows remaining is: {self.arrows}"

    def run(self):
        return "Ran really fast"


# Multiple Inheritance Class
class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)

    def say_my_name(self):
        return f"My name is Captain {self.name}"


# Hybrid Class instance
hybrid_one = Hybrid("Vyom", 95, 389)

print(hybrid_one.run())  # Ran really fast
print(hybrid_one.check_arrows())  # Number of arrows remaining is: 389
print(hybrid_one.attack())  # Attacking with the power of 95
print(hybrid_one.say_my_name())  # My name is Captain Vyom
print(hybrid_one.sign_in())  # User logged in !!
