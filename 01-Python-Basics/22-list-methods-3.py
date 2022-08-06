my_list = [
    "Tello",
    "Hi",
    "There",
    23,
    45,
    78,
    99,
    45,
    "Good",
    "Bad",
    "Ugly",
    "Great",
    "Movie",
]

my_string_list = [
    "Tello",
    "Hi",
    "There",
    "Good",
    "Bad",
    "Ugly",
    "Great",
    "Movie",
]

my_number_list = [34, 72, 23, 89, 99, 56, 12, 67]

# ----------------
# Some more methods
# -----------------

# ---------
# sort()
# -----------
my_string_list.sort()
my_number_list.sort()

print(my_string_list.sort())  # None
print(my_number_list.sort())  # None


print(
    my_string_list
)  # ['Bad', 'Good', 'Great', 'Hi', 'Movie', 'Tello', 'There', 'Ugly']
print(my_number_list)  # [12, 23, 34, 56, 67, 72, 89, 99]

# -----------
# sorted()
# -------------
# IT DOES NOT MODIFIES THE LIST,
# instead, it produces a COPY of the list just like my_cart[:], and also a SORTED list
my_cart = ["a", "x", "n", "t", "v", "b", "t"]
copied_and_sorted_cart = sorted(my_cart)

print(copied_and_sorted_cart)  # ['a', 'b', 'n', 't', 't', 'v', 'x']
print(my_cart)  # ['a', 'x', 'n', 't', 'v', 'b', 't']

# -----------
# copy()
# -----------
my_basket = ["The", "Good", "The", "Bad", "And", "The", "Ugly"]
my_basket_copy = my_basket.copy()
print(my_basket_copy)  # ['The', 'Good', 'The', 'Bad', 'And', 'The', 'Ugly']


# -----------
# reverse()
# -----------
shiv_mantra = ["Om", "Namah", "Shivaaye"]
new_mantra = shiv_mantra.reverse()

print(new_mantra)  # None
print(shiv_mantra)  # ['Shivaaye', 'Namah', 'Om']

# --------------------------
# sort() and then reverse()
# --------------------------
basket = ["a", "x", "c", "b", "d", "e", "d"]

basket.sort()
basket.reverse()

print(basket)  # ['x', 'e', 'd', 'd', 'c', 'b', 'a']
