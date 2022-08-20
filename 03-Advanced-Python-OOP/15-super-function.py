# -----------------------------------------------
# Method -1


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return "User logged in"


class Wizard(User):
    def __init__(self, name, power, email):
        self.name = name
        self.power = power
        self.email = email

    def attack(self):
        return f"Wizard {self.name} has an attack the power of {self.power}"


wizard1 = Wizard("Witcher", 100, "witcher@gmail.com")
print(wizard1.email)


# ----------------------------------------------------
# Method -2
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return "User logged in"


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        return f"Wizard {self.name} has an attack the power of {self.power}"


wizard1 = Wizard("Witcher", 100, "witcher@gmail.com")
print(wizard1.email)  # witcher@gmail.com

# ----------------------------------------
# Method -3 : Using super() function
# -----------------------------------------


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return "User logged in"


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        return f"Wizard {self.name} has an attack the power of {self.power}"


wizard1 = Wizard("Witcher", 100, "witcher@gmail.com")
print(wizard1.email)  # witcher@gmail.com
