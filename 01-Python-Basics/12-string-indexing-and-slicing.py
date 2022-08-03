greeting = "Hello there"

print(greeting[0])
print(greeting[1])
print(greeting[2])

print(greeting[-1])
print(greeting[-2])


print(greeting[0:2])  # 01 denotes He

print(greeting[0:])  # Hello there
print(greeting[1:])  # ello there

print(greeting[0:-1])  # Hello ther

print(greeting[:])  # Hello there
print(greeting[:3])  # Hel

# ----------------
# With Step size
# ----------------
# [start : stop: step_size]
print(greeting[0:6:2])  # Hlo
print(greeting[0::2])  # Hlotee
print(greeting[0::1])  # Hello there

# ------------------------------
# Reverse the string: Important
# ------------------------------
print(greeting[::-1])  # ereht olleH
print(greeting[::-2])  # eetolH
