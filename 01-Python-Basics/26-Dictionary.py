# Dictionary: Its a Data Type in Python as well as a Data Structure
#  They are an unordered list with a Key: Value Pair

my_dict = {
    "first_name": "John",
    "age": 56,
    "job": "Programmer",
    "last_name": "Smith",
    "serial": [23, 45, 67],
    "nice": True,
}

# print(my_dict["age"])
# print(my_dict["serial"][0])

my_list = [
    {
        "first_name": "Peter",
        "age": 34,
        "job": "Agent",
        "last_name": "Quinn",
        "serial": [2, 4, 7],
        "has_magic": True,
    },
    {
        "first_name": "Eddie",
        "age": 34,
        "job": "Agent",
        "last_name": "Burns",
        "serial": [179, 46, 67],
        "nice": True,
    },
]

# print(my_list[0]["serial"][2])

# -----------------------------------------------------------
# Dictionary Keys: Needs to be IMMUTABLE and Must be Unique
# -----------------------------------------------------------
my_info = {123: [56, "Nice", "Guy"], True: "Hello", "is_magic": True}

# ⭐ Lists ❌cannot be used as a key: as they are MUTABLE

# my_info = {123: [56, "Nice", "Guy"], True: "Hello", [100]: "Hundred"} # TypeError: unhashable type: 'list'

print(my_info["is_magic"])


#  IMPORTANT: Duplicate Key Overrides the previous key
another_dict = {"hello": "Greeting", "hello": [1, 2, 4]}

print(another_dict["hello"])
