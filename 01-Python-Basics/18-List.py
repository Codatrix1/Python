# ------------------
# Data Structure: 1
# ------------------

# --------------------------------------------
# Lists: Built-In or Implicit Data Structure
# --------------------------------------------
"""
list_one = [20, 30, 40, 50]
list_two = ["apple", "banana", "grapes", "mango"]
list_three = [
    1,
    2,
    3,
    56,
    "pineapple",
    "watermelon",
    True,
    12.56,
    89.23,
    "toys",
    "books",
]

amazon_cart = ["notebooks", "pencil", "glasses", "pen"]
print(amazon_cart[0])  # notebooks
print(amazon_cart[-1])  # pen

"""

# --------------
#  List Slicing
# --------------

# ---------------------
# LISTS are MUTABLE ✔
# ----------------------
"""


my_shopping_list = [
    "cards",
    "newspaper",
    "eraser",
    "apple",
    "watermelon",
    "pineapple",
    "phone",
]

print(my_shopping_list[0:2])  # ['cards', 'newspaper']
print(my_shopping_list[0::2])  # ['cards', 'eraser', 'watermelon', 'phone']

my_shopping_list[0] = "new_cards"
print(
    my_shopping_list
)  # ['new_cards', 'newspaper', 'eraser', 'apple', 'watermelon', 'pineapple', 'phone']

print(my_shopping_list[0:3])  # ['new_cards', 'newspaper', 'eraser']

"""

# ------------------------------------
#  Important: Making a Copy of a list
# ------------------------------------
#  WRONG WAY ❌: This modifies the original list
"""
first_list = ["apple", "banana", "orange"]
first_list_copy = first_list

print(first_list)
print(first_list_copy)

first_list_copy[0] = "grapes"

print(first_list)
print(first_list_copy)

"""


#  CORRECT WAY ✔: Creates a copy and keeps the original list intact
first_list = ["apple", "banana", "orange"]
first_list_copy = first_list[:]

print(first_list)
print(first_list_copy)

first_list_copy[0] = "grapes"

print(first_list)
print(first_list_copy)
