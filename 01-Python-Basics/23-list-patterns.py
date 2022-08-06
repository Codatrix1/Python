basket = ["a", "x", "c", "b", "d", "e", "d"]

basket.sort()
basket.reverse()

print(basket[::-1])  # ['a', 'b', 'c', 'd', 'd', 'e', 'x']
print(basket)  # ['x', 'e', 'd', 'd', 'c', 'b', 'a']

# -------------------
# range(start, stop)
# -------------------
print(list(range(1, 50)))
print(list(range(50)))

# -------------------
# join()
# -------------------
sentence = "+".join(["Hello", "There", "All"])
print(sentence)
