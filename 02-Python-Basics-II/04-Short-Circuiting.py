# ------------------
# Short Circuiting
# ------------------


# with "or"
is_user = True
is_friend = False

if is_user or is_friend:
    print("Hello there")  # Hello there


# with "and"
is_user = False
is_friend = True

if is_user and is_friend:
    print("Shorted")  # No output


print(1 > 2 < 3 > 4)  # False
