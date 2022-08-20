# Parent/Base Class
class User:
    def sign_in(self):
        return "User logged in !!"


# Children/Derived Classes: With Inherited Properties
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


# -----------------
# IMPORTANT ⭐⭐
# -----------------
print(
    wizard1.__class__
)  # <class '__main__.Wizard'> # It also inherites the Python Base Class

# -----------------
# isinstance
# -----------------
# isinstance(class_instance, Main Class or Parent Class or Python Base Object Class)
print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))  # True
print(isinstance(wizard1, object))  # True

# -----------------
# issubclass
# -----------------
# issubclass(child_class, parent_class)
print(issubclass(Wizard, User))  # True
print(issubclass(Wizard, object))  # True
