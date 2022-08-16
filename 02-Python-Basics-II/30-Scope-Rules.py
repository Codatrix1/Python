# Scope - what variables do I ahve access to?
# Python is function scoped


a = 1


def confusion():
    a = 5
    return a


print(confusion())  # 5 : Its function scoped value
print(a)  # 1 : Its globally scoped value


# Rules for Scope: The Scope Chain
# 1) Start with the Local scope
# 2) Go up ⬆ the scope chain and search in the Parent scope
# 3) Go up ⬆⬆ the scope chain and search the Global scope
# 4) Go up ⬆⬆⬆ the scope chain and search in Python Built-in scope

# -----------------
a = 1


def parent():
    a = 10

    def confusion():
        return a

    return confusion()


print(parent())  # 10
print(a)  # 1

# -----------------------
a = 1


def parent():
    a = 10

    def confusion():
        a = 15
        return a

    return confusion()


print(parent())  # 15
print(a)  # 1

# -----------------------
a = 1


def parent():
    a = 10

    def confusion():
        return sum

    return confusion()


print(parent())  # <built-in function sum>
print(a)  # 1
