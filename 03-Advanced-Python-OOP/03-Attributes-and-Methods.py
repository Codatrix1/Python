class PlayerCharacter:

    # Constructor function: self is like "this" keyword in JavaScript
    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name  # attributes
            self.age = age

    # Class Object Attribute
    membership = True

    # method
    def shout(self):
        return f"My name is {self.name}"

    # method
    def greeting(self, greet):
        return f"{greet} {self.name}"


# Instance of class
player1 = PlayerCharacter("Andy", 30)
player2 = PlayerCharacter("John", 38)
player2.level = 50

print(player1.name)  # Andy
print(player1.membership)  # True

print(player1.shout())  # My name is Andy
print(player2.shout())  # My name is John

print(player1.greeting("Hello"))  # Hello Andy
print(player2.greeting("Namaste"))  # Namaste John
