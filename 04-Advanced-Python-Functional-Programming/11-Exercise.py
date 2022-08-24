# Find Duplicates in the list using Comprehensions and print it as a list

some_list = ["a", "b", "c", "b", "n", "m", "n"]

duplicates = list(set([value for value in some_list if some_list.count(value) > 1]))
print(duplicates)
