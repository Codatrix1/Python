# Find the highest even number from the given list


def highest_even(my_list):
    even_list = []

    for eachItem in my_list:
        if eachItem % 2 == 0:
            even_list.append(eachItem)

    return max(even_list)


print(highest_even([11, 2, 3, 4, 14, 8, 10]))
