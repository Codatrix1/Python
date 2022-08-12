# -------------
# enumerate - very useful when index counter is required while looping through an iterable
# -------------

my_dict = {"name": "John", "age": 54}
my_set = {1, 2, 3}
my_list = [23, 45, 56]
my_tuple = (456, 678, 567)

# -----------------
# with Dictionary
# ----------------

# for index, char in enumerate(my_dict.items()):
#     print(index, char)

# for index, char in enumerate(my_dict.keys()):
#     print(index, char)

# for index, char in enumerate(my_dict.values()):
#     print(index, char)

# -----------------
# with List
# ----------------

for index, char in enumerate(my_list):
    print(index, char)

# -----------------
# with Set
# ----------------

for index, char in enumerate(my_set):
    print(index, char)
# -----------------
# with Tuple
# ----------------

for index, char in enumerate(my_tuple):
    print(index, char)

# --------------------------------------
# Find the index of 25 in the range 0, 30
# ---------------------------------------

for index, char in enumerate(range(1, 30)):
    if char == 25:
        print(f"The index of 25 is: {index}")

for index, char in enumerate(list(range(10))):
    if char == 5:
        print(f"The index of 5 is: {index}")
