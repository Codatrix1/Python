class PlayerCharacter:

    # init is the constructor: with default params
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
