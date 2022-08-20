# Polymorphism

"""
Now in Python, this idea of polymorphism refers to the way in which object classes can share the same method name.
But those method names can act differently based on what object calls them and can be used in different forms.

"""

# Parent/Base Class
class User:
    def sign_in(self):
        return "User logged in !!"

    # def attack(self):
    #     print("No attack power")  # ⭐


# Children/Derived Classes: With Inherited Properties
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        # User.attack(self) # ⭐
        return f"Wizard {self.name} has an attack the power of {self.power}"


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        return f"Number of Arrows left with the Archer {self.name}: {self.num_arrows}"


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 25)

# ---------------------------------------------------
# Same method "attack" called by different Objects
# ----------------------------------------------------
print(wizard1.attack())  # Wizard Merlin has an attack the power of 50
print(archer1.attack())  # Number of Arrows left with the Archer Robin: 25

# ----------------------------------------
# Creating a Function to call the Methods
# -----------------------------------------
def player_attack(character_name):
    return character_name.attack()


print(player_attack(wizard1))  # Wizard Merlin has an attack the power of 50
print(player_attack(archer1))  # Number of Arrows left with the Archer Robin: 25

# ----------------
# Using "for" Loop
# ----------------
for eachItem in [wizard1, archer1]:
    print(eachItem.attack())


"""
Wizard Merlin has an attack the power of 50
Number of Arrows left with the Archer Robin: 25

"""

# -----------------------------------------------------------------------
# ⭐ Using same method as a default in the parent class as well as a subclass
# ------------------------------------------------------------------------

# print(wizard1.attack())
