user_info = {
    "first_name": "Peter",
    "age": 34,
    "job": "Agent",
    "last_name": "Quinn",
    "serial": [2, 4, 7],
    "has_magic": True,
}

# print(user_info["password"])  # KeyError: 'password'

print(user_info.get("password"))  # None

print(user_info.get("password", 66))  # 66

# --------------------------------
# Another way to create Dictionary
# --------------------------------

user_two = dict(name="BonBon")
print(user_two)
print(user_two["name"])
