# ---------------------------------------------------
# What is Encapsulation and why do we require it?
# ---------------------------------------------------

"""
Encapsulation is the binding of data and functions that manipulate that data. And we encapsulate into one big object so that we keep everything in this box that users or code or other machines can interact with.
And this data and functions are what we call attributes and methods.

Because of encapsulation, we have all this functionality available to us, all these methods that we can access.

Why do we want to package data and functions into attributes and methods?

Well, because this gives us extra power, right?

If, for example, this player character doesn't have any actions, any methods and just had attributes.
Well, in that case, this is kind of like a dictionary, right?
"""


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return "Run"

    def intro(self):
        return f"My name is {self.name} and I am {self.age} years old"


player1 = PlayerCharacter("John", 33)
print(player1)
print(player1.intro())


# ---------------------------------------------------------------------------------
# There is no difference between the below two, just the way that we access info
# ---------------------------------------------------------------------------------
class AnotherPlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age


player2 = AnotherPlayerCharacter("Peter", 30)
print(player2.name)  # Peter
print(player2.age)  # 30

player3 = {"name": "Peter", "age": 30}
print(player3["name"])  # Peter
print(player3["age"])  # 30
