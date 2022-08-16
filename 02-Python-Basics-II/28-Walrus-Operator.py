# The walrus operator :=

# Assigns values to variables as part of a larger expression
"""
Its a way for us to minimize doing calculations that are similar,
    let's say in case of an "if" statement or "while" statement 
    where we want to do something based on a condition and calculate that value again

"""
greeting = "Hellooooooooo"

if (n := len(greeting)) > 10:
    print(f"Too long {n} elements")

while (n := len(greeting)) > 1:
    print(n)
    greeting = greeting[:-1]
