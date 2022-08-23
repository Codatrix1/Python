from functools import reduce


my_list = [1, 2, 3]


def add_numbers(acc, num):
    print(acc, num)
    return acc + num


result1 = reduce(add_numbers, my_list, 0)
print(result1)

"""
0 1
1 2 
3 3 
6  

"""
result2 = reduce(add_numbers, my_list, 10)
print(result2)

"""
10 1
11 2
13 3
16

"""
