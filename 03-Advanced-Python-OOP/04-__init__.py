class PlayerCharacter:

    # init is the constructor or the initial state of a Class: with default params
    # Note: The __init__() function is called automatically every time the class is being used to create a new object.
    def __init__(self, name="anonymous", age=0):
        if age > 18:
            self.name = name  # attribute
            self.age = age

    # method
    def shout(self):
        return f"My name is {self.name}"


player1 = PlayerCharacter("Tom", 10)
player2 = PlayerCharacter("Riddle", 29)

print(
    player1.shout()
)  # AttributeError: 'PlayerCharacter' object has no attribute 'name'

print(player2.shout())  # My name is Riddle
