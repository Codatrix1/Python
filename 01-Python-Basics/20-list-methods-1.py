basket = [1, 2, 3, 4, 5]
print(len(basket))

# Important: LISTS ARE MUTABLE

# ---------------------------
# Adding values to a list
# ----------------------------

# append()
new_basket_one = basket.append(100)
print(new_basket_one)  # None
print(basket)  # [1, 2, 3, 4, 5, 100]

# insert(): Insert value at specific index
new_basket_two = basket.insert(1, 200)
print(new_basket_two)  # None
print(basket)  # [1, 200, 2, 3, 4, 5, 100]

# extend(iterable)
new_basket_three = basket.extend(["Hello", "There"])
print(new_basket_three)  # None
print(basket)  # [1, 200, 2, 3, 4, 5, 100, 'Hello', 'There']


# ---------------------------
# Removing values from a list
# ----------------------------

# pop(): Removes the last element from the list
new_basket_four = basket.pop()
print(new_basket_four)  # There
print(basket)  # [1, 200, 2, 3, 4, 5, 100, 'Hello']

new_basket_five = basket.pop()
print(new_basket_five)  # Hello
print(basket)  # [1, 200, 2, 3, 4, 5, 100]

# pop(index): Removes the last element from specific
basket.pop(1)  # removes from a specific index
print(basket)  # [1, 2, 3, 4, 5, 100]

# remove(specific_value)
basket.remove(100)  # [1, 2, 3, 4, 5]
print(basket)

# clear()
new_basket_six = basket.clear()
print(new_basket_six)  # None
print(basket)  # []
