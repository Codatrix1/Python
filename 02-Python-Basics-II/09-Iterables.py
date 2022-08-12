# Iterables - String, List, Tuples, Dictionary, Set
# Iterate -> Check each item one by one

user_details = {"name": "John", "age": 54, "job": "Programmer", "has_magic": True}

# for eachItem in user_details:
#     print(eachItem)

# ---------------------------
# 1. Getting Key: Value Pairs
# ---------------------------

for eachItem in user_details.items():
    print(eachItem)

"""
Output: 

('name', 'John')
('age', 54)
('job', 'Programmer')
('has_magic', True)

"""

# ---------------------------
# 2. Getting Values Only
# ---------------------------

for eachItem in user_details.values():
    print(eachItem)

# ---------------------------
# 3. Getting Keys Only
# ---------------------------

for eachItem in user_details.keys():
    print(eachItem)

for eachItem in user_details:
    print(eachItem)

# ---------------------------
# 4. Getting them separately
# ---------------------------

for key, value in user_details.items():
    print(f"{key}: {value}")

# -------------------------------------
# 5. Trying to iterate over an integer
# -------------------------------------
for eachItem in 45:
    print(eachItem)  # TypeError: 'int' object is not iterable
