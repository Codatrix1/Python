greeting = "hello"
print(len(greeting))

# Built in methods
print(greeting.capitalize())

# --------------------
# Some more methods
# --------------------
my_quote = "to be or not to be"

print(my_quote.upper())  # TO BE OR NOT TO BE
print(my_quote.capitalize())  # To be or not to be
print(my_quote.find("be"))  # 3: Provides the index of the first match/occurence
print(my_quote.replace("be", "ME"))  # to ME or not to ME

# Our original string the same: Strings are IMMUTABLE
print(my_quote)  # to be or not to be
