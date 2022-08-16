# -----------------------------------------------------
# (*args, **kwargs) - (arguments, keyword_arguments)
# -----------------------------------------------------

# -----------------------------------------------
# *args - can recieve any number of arguments
# ----------------------------------------------
def super_func(*args):
    print(args)  # (1, 2, 3, 4, 5)
    print(*args)  # 1 2 3 4 5
    return sum(args)


print(super_func(1, 2, 3, 4, 5))  # 15

# -----------------------------------------------
# **kwargs
# allows any number of keyword arguments
# gives a dictionary as keyword args and use them however we want
# ----------------------------------------------
def super_func(*args, **kwargs):
    print(kwargs)  # {'num1': 5, 'num2': 10}
    return sum(args)


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))  # 15

# ------------------
# (*args, **kwargs)
# ------------------
def super_func(*args, **kwargs):
    total = 0
    for eachItem in kwargs.values():
        total += eachItem
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))  # 30


# ------------------------
# Order of parameters Rule:
# -------------------------

# (params, *args, default_params, **kwargs)


def twin_peaks(name, *args, age=34, **kwargs):
    total = 0
    for eachItem in kwargs.values():
        total += eachItem
        dialogue = f"{name} has {sum(args) + total} pines and he is {age} years old"

    return dialogue


print(
    twin_peaks("Andy", 1, 2, 3, 4, 5, first_num=10, second_num=5)
)  # Andy has 30 pines and he is 34 years old

print(
    twin_peaks("Andy", 1, 2, 3, 4, 5, age=30, first_num=10, second_num=5)
)  # Andy has 30 pines and he is 30 years old
