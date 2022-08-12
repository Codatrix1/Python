# ----------------------------------
# Equality Check: Checks the value
# ---------------------------------

# print(True == 1)  # True
# print("1" == 1)  # False
# print("" == 1)  # False
# print("" == 0)  # False
# print("" == bool(0))  # False
# print([] == 1)  # False
# print(10 == 10.0)  # True
# print([] == [])  # True

# -----------------------
# Points to location in memory
# -----------------------
print(True is 1)  # False
print("1" is 1)  # False
print("" is 1)  # False
print("" is 0)  # False
print("" is bool(0))  # False
print([] is 1)  # False
print(10 is 10.0)  # False
print([] is [])  # False

print(True is True)  # True
print("1" is "1")  # True

print([1, 2, 3] is [1, 2, 3])  # False: Since its a data structure

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # False
print(a == b)  # True
