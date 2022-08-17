# ----------------------------
# b is part of the local scope
# ----------------------------
def confusion(b):
    return b


print(confusion(200))

# -------------------
# using global scope
# -------------------
total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())

# -------------------
# Dependecy Injection
# -------------------
total = 0


def count(total):
    total += 1
    return total


final_count = count(count(count(total)))
print(final_count)  # 3
