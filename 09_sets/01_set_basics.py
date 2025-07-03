# Sets in Python:
# - Unordered collections of unique items.
# - Defined with curly braces {}.
# - Do not allow duplicates.
# - Immutable (elements can't be modified).

# Creating a set with duplicates
s = {2, 4, 2, 6}
print(s)  # Output: {2, 4, 6} – duplicates are removed

# Set with mixed data types
info = {"Carla", 19, False, 5.9, 19}
print(info)  # Output: unordered unique elements

# Creating an empty set
a = set()
print(type(a))  # <class 'set'>

# Iterating through a set
for value in info:
    print(value)
