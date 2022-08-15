# with Default Params
def greeting(name="John Smith", emoji="😊"):
    print(f"Hello my friend {name} {emoji}")


"""

# Positional Args - Arguments need to be in proper positions
greeting("John", "🙂")
greeting("Peter", "👋")

# Keyword Args
greeting(emoji="🌟", name="Quinn")

"""
greeting(emoji="🌟", name="Quinn")  # Hello my friend Quinn 🌟

greeting()  # Hello my friend John Smith 😊
greeting("Morty", "🐛")  # Hello my friend Morty 🐛
greeting("Rick")  # Hello my friend Rick 😊
