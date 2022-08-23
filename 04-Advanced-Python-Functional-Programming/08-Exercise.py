# Print Squares using lambda
my_list = [5, 4, 3]

squared_list = list(map(lambda item: item**2, my_list))
print(squared_list)  # [25, 16, 9]

# List Sorting based on the second value of the tuple
another_list = [(0, 2), (10, -1), (4, 3), (9, 9)]

# another_list.sort()
# print(another_list)

another_list.sort(key=lambda item: item[1])
print(another_list)  # [(10, -1), (0, 2), (4, 3), (9, 9)]
