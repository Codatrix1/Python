# nonlocal Keyword is used generally in Closures


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner: ", x)

    inner()
    print("outer: ", x)


outer()

"""
inner:  nonlocal
outer:  nonlocal
"""

# -----------------------------------------
def outer():
    x = "local"

    def inner():
        # nonlocal x
        x = "nonlocal"
        print("inner: ", x)

    inner()
    print("outer: ", x)


outer()

"""
inner:  nonlocal
outer:  local
"""
