# Dunder Methods or Magic Methods:

"""
They allow us to use Python specific functions on objects created through our class
like __str__, __class__, __main__

They can be customised if required as per needs

"""


class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {"name": "Bobo", "has_pets": True}

    # Dunder method __str__ modified
    def __str__(self):
        return f"{self.color}"

    # Dunder method __len__ modified
    def __len__(self):
        return 600

    # Dunder method __del__ modified: Not Recommended: Causes Bugs 🐛
    # def __del__(self):
    #     print("Deleted!!")
    #     return

    # Dunder method __call__ modified
    def __call__(self):
        return "Yes Calling !"

    # Dunder method __getitem__
    def __getitem__(self, index):
        return self.my_dict[index]


# Class Instance
action_figure = Toy("Blue", 0)

# Original Output
print(action_figure)  # <__main__.Toy object at 0x000001FEBDA27D60>
print(action_figure.__str__())  # <__main__.Toy object at 0x000001FEBDA27D60>

# Modified for this Object only: __str__, our new output
print(action_figure)  # Blue
print(action_figure.__str__())  # Blue
print(str(action_figure))  # Blue


# Some more

# __len__
print(len(action_figure))  # 600

# __del__
# del action_figure  # Deleted

# __call__
print(action_figure())  # Yes Calling !

# __getitem__
print(action_figure["name"])  # Bobo
print(action_figure.__getitem__("name"))  # Bobo
