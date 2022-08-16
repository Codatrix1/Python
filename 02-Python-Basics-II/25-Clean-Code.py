# -----------------------
# Odd or even function
# -----------------------


def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_even(num):
    if num % 2 == 0:
        return True
    return False


# Evaluates True or False since its an expression
def is_even(num):
    return num % 2 == 0


print(is_even(22))
