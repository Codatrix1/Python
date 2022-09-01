"""
Decorator Pattern: 

Now, the reason this is called a decorator, it's because it's a famous pattern in programming. It's called the decorator pattern.
And this is the decorator pattern. It gives our decorator flexibility so that we're able to pass as many arguments as we want into our wrapper function by using *args and **kwargs and then unpacking them like this inside of a function.

And this syntax, let's say if we didn't even have the print statements, this syntax is why decorators are so powerful.
By just using these lines of code, we're able to add functionality using the decorator pattern to decorate our functions.

And the decorator patterns are used all over programming.

So it's a very, very powerful concept.
"""


def my_decorator(some_func):
    def wrapper(*args, **kwargs):
        some_func(*args, **kwargs)

    return wrapper


@my_decorator
def hello(msg, emoji="👋"):
    print(msg, emoji)


hello("Hiiii")
