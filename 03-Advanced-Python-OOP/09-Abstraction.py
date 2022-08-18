# Abstraction :

"""
Abstraction means hiding of information or abstracting away information and giving access to only what's necessary.
So whatever the user or the programmer or the machine is interested in, that's the only thing we give access to

"""


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return "Run"

    def intro(self):
        return f"My name is {self.name} and I am {self.age} years old"


player1 = PlayerCharacter("Quinn", 32)

# Abstraction: We dont need to know, how the code is being implemented, we just want access to its methods or attributes

print(player1.intro())  # My name is Quinn and I am 32 years old
print((1, 2, 3, 4, 1, 1).count(1))  # 3
print(len(("Hello", "Friend")))  # 2

# Using a phone
# phone.take_picture() # we dont care how its implemented: thats Abstraction


# ----------------------------------------------------------------------------
# 😐🔥 GOTCHA : But the code can be manipulated here. How can we solve this?
# ----------------------------------------------------------------------------


class TestClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return "Run"

    def intro(self):
        return f"My name is {self.name} and I am {self.age} years old"


player2 = TestClass("Jane", 20)
print(player2.intro())  # My name is Jane and I am 20 years old

# Modifying the attributes and Methods
player2.name = "!!!"
player2.intro = "HELLOOOO"

print(player2.intro())  # TypeError: 'str' object is not callable
