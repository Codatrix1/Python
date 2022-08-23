from functools import reduce


# 1 Capitalize all of the pet names and print the list
my_pets = ["sisi", "bibi", "titi", "carla"]


def func_one(item):
    return item.capitalize()


result1 = list(map(func_one, my_pets))
print(result1)  # ['Sisi', 'Bibi', 'Titi', 'Carla']


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

print(
    list(zip(my_strings, sorted(my_numbers)))
)  # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def func_two(item):
    return item > 50


print(list(filter(func_two, scores)))  # [73, 65, 76, 100, 88]

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
all_num = my_numbers + scores
print(all_num)


def combine_func(acc, eachItem):
    return acc + eachItem


print(reduce(combine_func, all_num, 0))  # 456
