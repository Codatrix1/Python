is_magician = True
is_expert = False

# Check if magician and expert: "you are a master magician"

# Check if magician but not expert: "At least you are getting there"

# if you are not a magician: "You need magical powers"

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("You are getting there")
elif not is_magician:
    print("You need magical powers")
else:
    print("Bye! Bye!")
