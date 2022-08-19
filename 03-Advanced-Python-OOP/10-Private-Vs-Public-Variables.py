# Private? No True Private variable in Python


class TestClass:
    def __init__(self, name, age):
        # Convention for Private variables
        self._name = name
        self._age = age

    def run(self):
        return "Run"

    def intro(self):
        return f"My name is {self._name} and I am {self._age} years old"


player2 = TestClass("Jane", 20)
print(player2.intro())  # My name is Jane and I am 20 years old

# Modifying the attributes and Methods
player2.name = "!!!"
player2.intro = "HELLOOOO"

print(player2.intro())  # TypeError: 'str' object is not callable
