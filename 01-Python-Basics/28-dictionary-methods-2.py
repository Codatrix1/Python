user_info = {
    "first_name": "Peter",
    "age": 34,
    "job": "Agent",
    "last_name": "Quinn",
    "serial": [2, 4, 7],
    "has_magic": True,
}

print("name" in user_info)  # False
print("first_name" in user_info)  # True

# ---------
# keys()
# ---------
print("greet" in user_info.keys())  # False
print("first_name" in user_info.keys())  # True

print("first_name" in user_info.keys())  # True

# ---------
# values()
# ---------
print("John" in user_info.values())  # False
print("Peter" in user_info.values())  # True

# ---------
# items(): Provides a list of tuples
# ---------
print(
    user_info.items()
)  # dict_items([('first_name', 'Peter'), ('age', 34), ('job', 'Agent'), ('last_name', 'Quinn'), ('serial', [2, 4, 7]), ('has_magic', True)])

# ---------
# copy()
# ---------
user_info_2 = user_info.copy()
print(user_info_2)

# ------------------
# pop("key_name")
# ------------------
print(user_info.pop("serial"))  # [2, 4, 7]
print(
    user_info
)  # {'first_name': 'Peter', 'age': 34, 'job': 'Agent', 'last_name': 'Quinn', 'has_magic': True}

# ----------------------------------
# popitem(): Removes the last item
# ---------------------------------
print(user_info.popitem())  # ('has_magic', True)
print(
    user_info
)  # {'first_name': 'Peter', 'age': 34, 'job': 'Agent', 'last_name': 'Quinn'}

# ------------------------
# update({"key": "value"})
# ------------------------
user_info.update({"age": 24})
print(
    user_info
)  # {'first_name': 'Peter', 'age': 24, 'job': 'Agent', 'last_name': 'Quinn'}


user_info.update({"new_key": "new_value"})
print(
    user_info
)  # {'first_name': 'Peter', 'age': 24, 'job': 'Agent', 'last_name': 'Quinn', 'new_key': 'new_value'}
