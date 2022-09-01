"""

HOC : Higher Order Functions

A higher order function is any function that either accepts a function as a parameter. Or returns a function.
And if you're thinking, hey, is that map() function that we talked about, is that a higher order function because it accepts a function?

Yep, that's a high order function. So is reduce(). Or filter(). These are all higher order functions.
"""


# HOC: Higher Order Function
def greet(func):
    return func()


def greet2():
    def func():
        return 16

    return func
