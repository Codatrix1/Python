first_list = [1, 2, 3, 4, 5]
second_list = ["apple", "mango", "banana", "orange", "cherry"]
third_list = [12.4, 34.6, 57.4, 36.2, 118.6]

zipped = list(zip(first_list, second_list, third_list))
print(
    zipped
)  # [(1, 'apple', 12.4), (2, 'mango', 34.6), (3, 'banana', 57.4), (4, 'orange', 36.2), (5, 'cherry', 118.6)]

# --------------------------------------------------------
first_list = [1, 2, 3, 4, 5]
second_list = ["apple", "mango", "banana"]
third_list = [12.4, 34.6, 57.4, 36.2, 118.6]

zipped = list(zip(first_list, second_list, third_list))
print(zipped)  # [(1, 'apple', 12.4), (2, 'mango', 34.6), (3, 'banana', 57.4)]
