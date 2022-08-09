# -----------
# Tuple
# -----------
# - Uses parenthesis
# - They are like lists but are IMMUTABLE
# - More performant than lists
# - Use case - Providing co-ordinates using geo-location feature
# - Tuple can be used as a KEY for Dictionary since Tuples are IMMUTABLE, unlike lists

my_tuple = (1, 2, 3, 4, 5)

# my_tuple[0] = 12
# print(my_tuple)  # TypeError: 'tuple' object does not support item assignment

# -----------------
# Tuple Methods
# ------------------
print(my_tuple[1])  # 2
print(5 in my_tuple)  # True

my_dict = {("a", "b"): [1, 2, 3], "greet": "Hello", "is_cool": True, "age": 12}
print(my_dict[("a", "b")])  # [1, 2, 3]

# --------------------------
# Some More Tuple Operations
# --------------------------
new_tuple = ("apple", "mango", "banana", "orange")

new_tuple_slice_one = new_tuple[1:2]
print(new_tuple_slice_one)  # ('mango',) : Outputs a comma if only one element

new_tuple_slice_two = new_tuple[1:4]
print(new_tuple_slice_two)  # ('mango', 'banana', 'orange')

# -------------------
# Unpacking a Tuple
# -------------------
x, y, z, *others = (1, 2, 3, 4, 5)
print(x)  # 1
print(y)  # 2
print(z)  # 3
print(others)  # [4, 5] : Outputs a list


# -------------------------------
# ⭐ Only 2 Tuple built-in methods
# ------------------------------


#  count(): counts the number of instances of the provided element
tuple_one = ("apple", "guava", "mango", "banana", "orange", "mango", "mango")

print(tuple_one.count("orange"))  # 1
print(tuple_one.count("mango"))  # 3


# index(): gives back the index for the first instance of the provided element
print(tuple_one.index("guava"))  # 1

# len(): Length of the tuple
print(len(tuple_one))  # 7
