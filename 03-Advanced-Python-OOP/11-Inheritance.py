# Inheritance

# Inheritance allows new objects to take on the properties of existing objects. So you can inherit classes.

# We are developing a game

# In this game, the players can be Wizards, Archers, Elves, Merchants
# They will have different powers according to their roles

# But they will have common functions like
# - All users must sign in
# - All users must have passwords
# The common properties will be INHERITED by all the types of users, except their different name, powers etc

# Users
# - Wizard
# - Archer
# - Merchant


# Parent/Base Class
class User:
    def sign_in(self):
        return "User logged in !!"


# Children/Derived Classes/Sub-Class: With Inherited Properties
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return f"Wizard {self.name} has an attack the power of {self.power}"


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        return f"Number of Arrows left with the Archer {self.name}: {self.num_arrows}"


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 25)

print(wizard1.sign_in())  # User logged in !!
print(wizard1.attack())  # Wizard Merlin has an attack the power of 50


print(archer1.sign_in())  # User logged in !!
print(archer1.attack())  # Number of Arrows left with the Archer Robin: 25
