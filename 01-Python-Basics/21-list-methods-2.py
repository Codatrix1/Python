my_shopping_cart = [
    "apple",
    "orange",
    "mango",
    "banana",
    24,
    78,
    63,
    754,
    "pine",
    "butter",
    "orange",
]


# ---------------------------
# Some More List Methods
# ----------------------------
# index(element): provides the index of the element
print(my_shopping_cart.index("mango"))  # 2

# index(element, start, stop)
# print(my_shopping_cart.index("pine", 0, 5))  # Error: ValueError: 'pine' is not in list
print(my_shopping_cart.index("pine", 0, -1))  # 8
print(my_shopping_cart.index("pine", 0, 9))  # 8


# count(): Count the no. of instances of the given element in a list
print(my_shopping_cart.count("orange"))  # 2


# ---------------------------
# Keywords in python
# ----------------------------
print("Hello" in my_shopping_cart)  # False
print("mango" in my_shopping_cart)  # True
print("w" in "Hellow there")  # True
