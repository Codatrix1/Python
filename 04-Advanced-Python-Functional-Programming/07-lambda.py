from functools import reduce

# lambda expressions

# - Anonymous functions
# - Used only once

# General Structure:
# lambda params: logic(params)

my_list = [1, 2, 3, 4, 5]

mapped_list = list(map(lambda item: item * 2, my_list))
print(mapped_list)  # [2, 4, 6, 8, 10]

accumulated_value = reduce(lambda acc, item: acc + item, my_list, 0)
print(accumulated_value)  # 15

filter_all_odds = list(filter(lambda item: item % 2 != 0, my_list))
print(filter_all_odds)  # [1, 3, 5]
