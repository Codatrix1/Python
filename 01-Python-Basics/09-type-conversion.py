my_number = 100
print(type(my_number))  # <class 'int'>

# Type Conversion
my_string = str(my_number)
print(my_string)  # 100
print(type(my_string))  # <class 'str'>

# Some more examples
# print("Hello" + " " + 100)  # Throws Error
print("Hello" + " " + str(100))  # Hello 100
