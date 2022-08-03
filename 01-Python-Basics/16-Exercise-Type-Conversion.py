# ----------------------------------------
# Write a program that calculates your age
# ----------------------------------------

birth_year = input("Please enter your birth year: ")
print(type(birth_year))  # <class 'str'>

current_age = 2022 - int(birth_year)
print(f"You are {current_age} years old !!")  # You are 33 years old !!

current_age = 2022 - float(birth_year)
print(f"You are {current_age} years old !!")  # You are 33.0 years old !!

# ------------------------------------------------------------------
# Booleans for a string evalutes to "True" == 1, Hence the output
# ------------------------------------------------------------------
current_age = 2022 - bool(birth_year)
print(f"You are {current_age} years old !!")  # You are 2021 years old !!
