# List Methods in Python

# Initial List
l = [11, 24, 1, 2, 3, 4, 5]
print("Original List:", l)

# (1) append() - Adds a single element at the end of the list
l.append(7)
print("After append(7):", l)

# (2) sort() - Sorts the list in ascending order (modifies original list)
l = [11, 24, 1, 2, 3, 4, 5]
l.sort()
print("After sort():", l)

# (3) reverse() - Reverses the order of elements in the list
l = [11, 24, 1, 2, 3, 4, 5]
l.reverse()
print("After reverse():", l)

# (4) index() - Returns the index of the first occurrence of a value
l = [11, 24, 1, 2, 3, 4, 5]
print("Index of 1:", l.index(1))      # Output: 2
print("Index of 11:", l.index(11))    # Output: 0

# (5) count() - Returns the number of occurrences of a value
l = [11, 1, 24, 1, 2, 3, 4, 5, 1]
print("Count of 1:", l.count(1))      # Output: 3

# (6) copy() - Returns a shallow copy of the list
l = [11, 24, 1, 2, 3, 4, 5]
print("Original list before modifying copy reference:", l)

# Using assignment (not recommended, modifies original list)
m = l
m[0] = 0
print("After modifying m (reference):", l)

# Using copy (recommended)
l = [11, 24, 1, 2, 3, 4, 5]
m = l.copy()
m[0] = 0
print("Original list after copy and modify m:", l)
print("Modified copy:", m)

# (7) insert() - Inserts an element at a specific index
l = [11, 24, 1, 2, 3, 4, 1]
l.insert(1, 899)   # Inserts 899 at index 1
print("After insert(1, 899):", l)

# (8) extend() - Adds elements of another iterable to the end of the list
l = [11, 24, 1, 2, 3, 4, 1]
m = [900, 1000, 1100]
l.extend(m)        # Extends list l with elements of list m
print("After extend([900, 1000, 1100]):", l)

# Alternative using + (does not modify original list)
# k = l + m
# print("Using + to combine lists:", k)
