# set_methods.py

# Joining Sets
# Sets in Python support operations like union and intersection similar to mathematics

# Union - returns a new set
s1 = {1, 2, 5, 6}
s2 = {3, 5, 7}
print("Union of s1 and s2:", s1.union(s2))  # {1, 2, 3, 5, 6, 7}

# Update - modifies the original set s1
s1.update(s2)
print("After s1.update(s2):", s1)  # {1, 2, 3, 5, 6, 7}
print("s2 remains unchanged:", s2)  # {3, 5, 7}

# Intersection 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# intersection = cities.intersection(cities2)
print("Intersection of cities:",cities.intersection(cities2))
# print("Intersection of cities:", intersection)

# Update 
cities.update(cities2)
print("After update:", cities)

# Symmetric Difference
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
symmetric_diff = cities.symmetric_difference(cities2)
print("Symmetric Difference:", symmetric_diff)

# Difference 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
difference = cities.difference(cities2)
print("Difference:", difference)

# isdisjoint() 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print("Is disjoint:", cities.isdisjoint(cities2))  # False

# issuperset()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
subset1 = {"Seoul", "Kabul"}
subset2 = {"Tokyo", "Madrid", "Delhi"}
print("Is superset of subset1:", cities.issuperset(subset1))  # False
print("Is superset of subset2:", cities.issuperset(subset2))  # True

# add()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print("After add:", cities)

# update() 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print("After update with multiple cities:", cities)

# remove() vs discard() 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")  # Removes Tokyo
print("After remove:", cities)
cities.discard("Tokyo2")  # No error even if item doesn't exist
print("After discard (no error):", cities)

# pop() 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print("After pop:", cities)
print("Popped item:", item)

# del keyword 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)  # this will raise: NameError

# clear()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print("After clear:", cities)  # set()

# Check Membership 
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
