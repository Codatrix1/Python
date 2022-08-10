# ------------------------------------
# Built-In Data Types in Python
# ------------------------------------

from traceback import print_tb


None
bool
int
float
complex
str

# ------------------------------------
# Built-In Data Structures in Python
# ------------------------------------

list
tuple
dict
set

# --------------
# Sets in Python
# --------------

# - Sets are Unordered structure of Unique objects: No duplicates
# - Use case - Let's say we have a users in our DB and we want only unique emails. We use set to store it

set_one = {1, 2, 3, 4, 5, 5}

set_one.add(100)
set_one.add(2)

print(set_one)  # {1, 2, 3, 4, 5, 100}

# -----------------------
# Convert List to a set
# -----------------------
my_list = ["apple", "mango", "banana", "orange", "pineapple", "apple"]
set_two = set(my_list)
print(set_two)  # {'pineapple', 'banana', 'orange', 'apple', 'mango'}


# -----------------------
# Set Operations
# -----------------------
print("orange" in set_two)  # True
print(len(set_two))  # 5

# -----------------------
# Convert Set to a List
# -----------------------
set_three = {1, 2, 3, 4, 5, 5}
print(list(set_three))  # [1, 2, 3, 4, 5]


# -----------------------
# copy()
# -----------------------
set_four = {1, 2, 3, 4, 5, 5}
set_four_copy = set_four.copy()
print(set_four_copy)  # {1, 2, 3, 4, 5}

# -----------------------
# clear()
# -----------------------
set_five = {1, 2, 3, 4, 5, 5}
set_five_new = set_five.copy()

set_five.clear()

print(set_five)  # set()
print(set_five_new)  # {1, 2, 3, 4, 5}
