# Comprehensions
# - Unique to Python
# - List Comprehensions
# - Set Comprehensions
# - Dictionary Comprehensions


my_list = []
for char in "hello":
    my_list.append(char)

print(my_list)  # ['h', 'e', 'l', 'l', 'o']

# Using List Comprehensions

"""
It's a way for us to quickly create lists with Python instead of looping and using append or things that we've seen before.
So it's a shorthand form for us to do things unique like this.
"""

# ---------------------------------------------------------------------------------------
# ⭐⭐ my_list = ["Expression" for "EachItem" in "iterable" if "some_other_conditional"
# ----------------------------------------------------------------------------------------

# Each character
my_list1 = [char for char in "hello"]
print(my_list1)

# Each number
my_list2 = [num for num in range(0, 20)]
print(my_list2)

# Multiply By 2
my_list3 = [num * 2 for num in range(0, 20)]
print(my_list3)

# Square
my_list4 = [num**2 for num in range(0, 20)]
print(my_list4)

# Make a Squared List and print Even Only: For a reversed list
my_list5 = [num**2 for num in reversed(range(0, 20)) if num % 2 == 0]
print(my_list5)

# ---------------------------------------------------------------------------------------
# ⭐⭐ my_list = ["Expression" for "EachItem" in "iterable" if "some_other_conditional"
# ----------------------------------------------------------------------------------------
