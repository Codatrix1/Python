# Formatted Strings

name = "John Smith"
age = 77
job = "programmer"

# --------------------
# New method: Python3
# --------------------
print(f"Hello {name} you are a {age} year old {job}")

# --------------------
# Old method: Python2
# --------------------
print("Hello {} you are a {} year old {}".format(name, age, job))
print("Hello {1} you are a {0} year old {2}".format(name, age, job))

print(
    "Hello {new_name} you are a {new_age} year old {new_job}".format(
        new_name="Peter", new_age=99, new_job="writer"
    )
)
