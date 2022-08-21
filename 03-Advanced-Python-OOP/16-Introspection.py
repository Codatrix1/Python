class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return "User logged in"


class Wizard(User):
    def __init__(self, name, power, email):
        # Super allows us to refer "User", as Parent Class, and we do not require us to pass "self" with init
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        return f"Wizard {self.name} has an attack the power of {self.power}"


wizard1 = Wizard("Witcher", 100, "witcher@gmail.com")
print(wizard1.email)  # witcher@gmail.com

# ----------------------------------------------------------------------
# Introspection: Ability to determine the type of an Object at Runtime
print(dir(wizard1))

"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attack', 'email', 'name', 'power', 'sign_in']

"""
