# ---------------
# List Unpacking
# ----------------

a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
print(b)
print(c)
print(other)

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
print(b)
print(c)
print(other)
print(d)
