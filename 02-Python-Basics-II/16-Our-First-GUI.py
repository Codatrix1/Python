# Exercise

# clean
# Readibility
# Predictability
# DRY Code

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

# Iteration required
# - For 1 -> "*"
# - For 0 -> " "

for row in picture:
    for pixel in row:
        if pixel == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")  # nned a new line after each row

fill = "$"
empty = " "


for row in picture:
    for pixel in row:
        if pixel:
            print(fill, end="")
        else:
            print(empty, end="")
    print("")  # nned a new line after each row
