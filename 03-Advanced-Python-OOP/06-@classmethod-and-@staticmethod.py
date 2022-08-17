"""

1) What is Python @classmethod?
In Python, the @classmethod decorator is used to declare a method in the class as a class method that can be called using 
ClassName.MethodName() 
The class method can also be called using an object of the class. The @classmethod is an alternative of the classmethod() function.

2) When should you use a Classmethod Python?
You can use class methods for any methods that are not bound to a specific instance but the class. In practice, you often use class methods for methods that create an instance of the class. When a method creates an instance of the class and returns it, the method is called a factory method.

3) Why do we use static methods?
A static method has two main purposes: For utility or helper methods that don't require any object state. Since there is no need to access instance variables, having static methods eliminates the need for the caller to instantiate the object just to call the method.

4) What is the difference between @staticmethod and Classmethod?
The difference between the Class method and the static method is: A class method takes cls as the first parameter while a static method needs no specific parameters. A class method can access or modify the class state while a static method can't access or modify it.

"""


class PlayerCharacter:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Class Object Attribute
    membership = True

    # Method
    def shout(self):
        return f"My name is {self.name}"

    @classmethod
    def add_numbers(cls, num1, num2):
        return cls("John", num1 + num2)

    @staticmethod
    def multiply(first_number, second_number):
        return f"The result is {first_number * second_number}"


print(
    PlayerCharacter.add_numbers(4, 6)
)  # <__main__.PlayerCharacter object at 0x0000024089BEFDC0>

Player3 = PlayerCharacter.add_numbers(25, 7)  # Gets assigned as "age" variable
print(Player3.name, Player3.age)  # John 32
print(
    f"My name is {Player3.name} and I am {Player3.age} years old"
)  # My name is John and I am 32 years old
