# -----------------------------------------------------
# Creating a Own Objects with a custom class in Python
# -----------------------------------------------------
class PlayerCharacter:
    # Constructor function: self is like "this" keyword in JavaScript
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return "Run Forest Run"


# Instance of class
player1 = PlayerCharacter("Andy", 30)
player2 = PlayerCharacter("John", 38)

# Accessing an attribute
print(player1.name, player1.age)  # Andy 30
print(player2.name, player2.age)  # John 38

# Accessing a method
print(player1.run())  # Run Forest Run

# Memory locations of Class instances
print(player1)  # <__main__.PlayerCharacter object at 0x000001E5AEA2FFD0>
print(player2)  # <__main__.PlayerCharacter object at 0x000001E5AEA2FEB0>

# Adding attributes to our instance
player1.level = 46

print(player1.level)  # 46
print(
    player2.level
)  # AttributeError: 'PlayerCharacter' object has no attribute 'level'
