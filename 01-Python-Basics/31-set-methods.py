# --------------------
# Common Set Methods
# --------------------

# .difference()
# .discard()
# .difference_update()
# .intersection()
# .isdisjoint()
# .union()
# .issubset()
# .issuperset()


# ------------------------------------------
# .difference(): DOES NOT MUTATE THE ORIGINAL
# ------------------------------------------
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8, 9, 10}

print(set_A.difference(set_B))  # {1, 2, 3}
print(set_A)  # {1, 2, 3, 4, 5}

# ----------------
# .discard()
# ----------------
set_A = {1, 2, 3, 4, 5}

set_A.discard(5)
print(set_A)  # {1, 2, 3, 4}

# --------------------------------------------
# .difference_update() : MUTATES THE ORIGINAL
# -------------------------------------------
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8, 9, 10}

set_A.difference_update(set_B)
print(set_A)  # {1, 2, 3}

# -------------------
# .intersection(): &
# -------------------
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8, 9, 10}

print(set_A.intersection(set_B))  # {4, 5}
print(set_A & set_B)  # {4, 5}

# --------------------------------------------
# .isdisjoint() : HAS ANY SAME ELEMENTS Or NOT
# --------------------------------------------
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8, 9, 10}

print(set_A.isdisjoint(set_B))  # False

set_C = {1, 2, 3, 4, 5}
set_D = {6, 7, 8, 9, 10}

print(set_C.isdisjoint(set_D))  # True

# ------------------------------------------------
# .union(): | : REMOVES DUPLICATES and Joins Two sets
# ------------------------------------------------
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8, 9, 10}

print(set_A.union(set_B))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set_A | set_B)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# ----------------
# .issubset()
# ----------------
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8, 9, 10}

print(set_A.issubset(set_B))  # False

set_C = {4, 5}
set_D = {4, 5, 6, 7, 8, 9, 10}

print(set_C.issubset(set_D))  # True

# ----------------
# .issuperset()
# ----------------
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8, 9, 10}

print(set_A.issuperset(set_B))  # False

set_C = {1, 2, 3, 4, 5}
set_D = {1, 2, 3}

print(set_C.issuperset(set_D))  # True
