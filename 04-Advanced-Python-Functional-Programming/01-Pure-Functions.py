# Functional Programming -
# Separation of Concerns -  DATA and FUNCTIONS are separate
# One Function does only one thing in the most efficient way

# Pure Functions
# - 1) Produces the same result everytime it runs - Does only one specific thing
# - 2) Does not produce any side-effects - No changes in other scopes
#      Its not fully possible since we want to see changes according to our code
# - 3) Less Buggy Code

# -----------------------------------------------
# Example: Multiply each number of a list by 2
# -----------------------------------------------

# Separate Data
wizard = {"name": "Witcher", "home_town": "Rivia"}

# ⭐ Pure Function: No Side Effects
def multiply_by_two(my_list):

    new_list = []

    for eachItem in my_list:
        new_list.append(eachItem * 2)
    return new_list


print(multiply_by_two([1, 2, 3, 4]))

# --------------------------------------------------------------------
# ⭐⭐ Impure Functions
# Side effects

# ------------
# Example 1
# ------------


def first_function(my_list):

    new_list = []

    for eachItem in my_list:
        new_list.append(eachItem * 2)
        # This is a side effect. We have no idea waht gets printed out
    return print(new_list)


print(first_function([1, 2, 3, 4]))

# -------------
# Example 2
# -------------

new_list = []  #  This is a side effect: Outside World Interaction


def second_function(my_list):
    for eachItem in my_list:
        new_list.append(eachItem * 2)
    return new_list


new_list = ""
print(
    second_function([1, 2, 3, 4])
)  # AttributeError: 'str' object has no attribute 'append'
