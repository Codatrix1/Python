# Decorators Practical Usage

"""

⭐ In Object Classes

@classmethod
@staticmethod

"""

# ⭐⭐ Performance Testing Decorator

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"Time elapsed: {t2-t1} seconds")
        return result

    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5


long_time()
