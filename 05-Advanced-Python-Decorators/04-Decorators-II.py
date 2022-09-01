"""
Remember, a decorator supercharges our function.
It's simply a function that wraps another function and enhances it or changes it.
"""


# Writing Custom Decorator Function
def my_decorator(some_func):
    def wrapper():
        print("*****")
        some_func()
        print("*****")

    return wrapper


@my_decorator
def hello():
    print("Hello Friend")


@my_decorator
def bye():
    print("See You Later !!")


def ring():
    print("Tring Tring!!")


hello()
bye()

phone = my_decorator(ring)
phone()
