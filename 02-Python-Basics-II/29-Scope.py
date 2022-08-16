# Scope - what variables do I ahve access to?
# Python is function scoped

# Global Scopes
name = "John"

if True:
    x = 10

print(name, x)

# Function Scope
def some_func():
    total = 100
    return total


# print(total)  # NameError
