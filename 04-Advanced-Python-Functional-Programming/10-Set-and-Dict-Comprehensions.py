# Set Comprehension

my_set1 = {char for char in "hello"}
my_set2 = {num for num in range(0, 20)}
my_set3 = {num**2 for num in range(0, 20) if num % 2 == 0}

# print(my_set1)
# print(my_set2)
# print(my_set3)

# Dictionary Comprehensions
simple_dict = {"a": 3, "b": 4}

my_dict1 = {key: value**2 for key, value in simple_dict.items()}
print(my_dict1)  # {'a': 9, 'b': 16}

my_dict2 = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict2)  # {'b': 16}

my_dict3 = {num: num * 2 for num in [1, 2, 3, 4]}
print(my_dict3)  # {1: 2, 2: 4, 3: 6, 4: 8}
