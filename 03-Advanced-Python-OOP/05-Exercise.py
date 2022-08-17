# Given the below class:
class Cat:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Class Object Attribute
    species = "mammal"


# 1 Instantiate the Cat object with 3 cats
Cat1 = Cat("Chuck", 2)
Cat2 = Cat("Norris", 4)
Cat3 = Cat("Hufflepuff", 5)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldest_cat(Cat1.age, Cat2.age, Cat3.age)} years old")
