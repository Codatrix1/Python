# map, filter, zip, and reduce

# map(function, *iterable)

my_list = [1, 2, 3, 4, 5]


def multiply_by_two(item):
    return item * 2


map_one = map(multiply_by_two, my_list)


print(list(map_one))  # [2, 4, 6, 8, 10]
print(my_list)  # [1, 2, 3, 4, 5]
