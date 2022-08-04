username = input("Please enter your name: ")
password = input("Please enter you password: ")

passwod_length = len(password)
hidden_password = "*" * passwod_length

print(
    f"Hey {username}, your password {hidden_password} is {passwod_length} letters long"
)
