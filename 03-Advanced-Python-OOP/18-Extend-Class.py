# Class to have a modified "__len__" dunder method


class SuperList:
    def __len__(self):
        return 1000


# Class instance
super_list1 = SuperList()

# Methods
print(len(super_list1))  # 1000

super_list1.append(
    "Hello"
)  # AttributeError: 'SuperList' object has no attribute 'append'
super_list1.append("Friend")

# Accessing value at index 1
print(super_list1[1])


# -------------------------------------------------------------------
# Extending "list" Class to have a modified "__len__" dunder method
# -------------------------------------------------------------------


class NewSuperList(list):
    def __len__(self):
        return 1000


# Class instance
new_super_list1 = NewSuperList()

# Methods
print(len(new_super_list1))  # 1000

new_super_list1.append("Hello")  # No errors
new_super_list1.append("Friend")  # No errors

# Accessing value at index 1
print(new_super_list1[1])  # Friend

print(issubclass(NewSuperList, list))  # True
print(issubclass(NewSuperList, object))  # True
print(issubclass(list, object))  # True
