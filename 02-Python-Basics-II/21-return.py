# A function is something that modifies something or reeturn something

# Best Practice for Functions
#  - A function should do one thing really well
#  - A function return something

"""

def sum(num1, num2):
    print("hello friend")
    num1 + num2


print(sum(10, 15))

"""


def my_sum(num1, num2):
    return num1 + num2
    print("Hello")  # Exists the code block immediately


first_result = my_sum(1, 5)
final_reult = my_sum(16, first_result)

print(final_reult)  # 22

# ---------------------
# Nesting functions
# --------------------


def first_function(num1, num2):
    def second_function(n1, n2):
        return n1 + n2

    return second_function(num1, num2)


total = first_function(10, 30)
print(total)  # 40
