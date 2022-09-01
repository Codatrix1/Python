# Error Handling

# -----------
# Example_1
# -----------
def my_sum_one(num1, num2):
    try:
        return num1 + num2
    except:
        return "Please enter numbers"


# print(my_sum_one(1, "2"))

# -----------
# Example_2
# -----------
def my_sum_two(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        return f"Please enter numbers: {err}"


# print(my_sum_two(1, "2"))

# -----------
# Example_3
# -----------
def my_division(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        return f"🔥 Error: {err}"


# print(my_division(1, 0))
print(my_division(1, "2"))
