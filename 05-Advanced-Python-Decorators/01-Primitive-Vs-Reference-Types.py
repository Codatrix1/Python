# ------------------
# Primitive Types
# ------------------
age = 30
old_age = age
age = 31

print(age)  # 31
print(old_age)  # 30

# -------------------------------------------------------
# Reference Types: Reference to memory address in HEAP
# -------------------------------------------------------
me = {"name": "John", "age": 24}

friend = me
friend["age"] = 42

print("Friend: ", friend)  # Friend:  {'name': 'John', 'age': 42}

print("Me:", me)  # Me: {'name': 'John', 'age': 42}
