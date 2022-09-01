"""
# ⭐⭐
A decorator in Python is a function that takes another function as its argument, and returns yet another function . Decorators can be extremely useful as they allow the extension of an existing function, without any modification to the original function source code. They supercharge our function and extends them to have extra functionalities.

Also in Python, functions are FIRST CLASS CITIZENS: They can be passed along like variables
"""

"""
@classmethod
@staticmethod

"""


def hello(func):
    return func()


def greet():
    return "Hello Friend"


welcome = hello(greet)

print(welcome)  # Hello Friend
