# OOP - Everything in Python is an Object
# - The main takeaway is that OOP is a paradigm, a way to think about our code, a way for us to structure
#   our code so that as it gets bigger and bigger, we're able to be organized, breaking the code into small objects
#   and combining that code to create something new.


print(type(5))  # <class 'int'>
print(type("John"))  # <class 'str'>
print(type(10.5))  # <class 'float'>
print(type(None))  # <class 'NoneType'>
print(type(True))  # <class 'bool'>
print(type([]))  # <class 'list'>
print(type({}))  # <class 'dict'>
print(type(()))  # <class 'tuple'>

# ------------------------------------
# Creating a custom class in Python
# ------------------------------------

# Class: Blue print: Naming convention starts with UPPERCASE Letter and then written using CamelCase notation
class BigObject:
    pass


# Class Instance: Object created using the blueprint
first_object = BigObject()
second_object = BigObject()
third_object = BigObject()

print(first_object)  # <__main__.BigObject object at 0x0000017DAA8FFFD0>
print(type(first_object))  # <class '__main__.BigObject'>
