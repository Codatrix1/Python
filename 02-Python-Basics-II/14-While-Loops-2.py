# ------------
# For Loop
# ------------

my_list = [1, 2, 3]

for eachItem in my_list:
    print(eachItem)

# ------------
# While Loop
# ------------

# Use Cases
# - when we don't know how many times we need to loop - For example - check through email list

# Example 1
i = 0
while i < len(my_list):
    print(my_list[i])
    i = i + 1


# Example 2
while True:
    response = input("Say something: ")
    if response == "bye":
        break
