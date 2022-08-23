# filter(function or None, iterable)

my_list = [1, 2, 3, 4, 5]


def only_odd(item):
    return item % 2 != 0


filter_one = filter(only_odd, my_list)


print(list(filter_one))  # [1, 3, 5]
print(my_list)  # [1, 2, 3, 4, 5]
