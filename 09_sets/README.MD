# Sets:- Sets are unordered collection of data items. They store multiple items in a single variable. Set items are seperated by commas and enclosed within curly brackets{}. Sets are unchangable, meaning you cannot change items of the set once created. sets do not contain duplicate items>  
# Python sets are unordered collections, meaning:                 #The items stored in a set do not maintain the order #in which they were added.Each time you print or loop through a set, the order might be different.
☑️ union()  
Combines all unique elements from two sets.

Removes duplicates automatically.

Syntax: set1.union(set2) or set1 | set2
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))     # Output: {1, 2, 3, 4, 5}
print(a | b)          # Output: {1, 2, 3, 4, 5}



☑️ intersection()
Returns common elements from both sets.

Syntax: set1.intersection(set2) or set1 & set2
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # Output: {3}
print(a & b)              # Output: {3}



# 🧮 Python Set Methods – Complete Example Guide

This repository contains a Python script demonstrating various **set operations and methods** using practical examples. Sets in Python are unordered, mutable collections of unique elements, and support powerful mathematical operations similar to sets in math.

---

## 📄 File Description

- **`set_methods.py`** – This script includes:
  - Basic set operations (union, intersection, difference)
  - In-place updates
  - Membership checks
  - Element manipulation (`add`, `remove`, `discard`, `pop`)
  - Deletion and clearing methods
  - Advanced methods like `isdisjoint()`, `issuperset()`, etc.

---

## 🧪 Set Methods Covered

| Method | Description |
|--------|-------------|
| `union()` | Returns a new set with all items from both sets |
| `update()` | Adds items from another set (modifies in-place) |
| `intersection()` | Returns common items between two sets |
| `symmetric_difference()` | Items present in one set but not both |
| `difference()` | Items in one set but not in another |
| `isdisjoint()` | Checks if two sets have no items in common |
| `issuperset()` | Checks if one set contains all elements of another |
| `add()` | Adds a single element to the set |
| `remove()` | Removes a specific element (raises error if not found) |
| `discard()` | Removes a specific element (no error if not found) |
| `pop()` | Removes and returns an arbitrary element |
| `clear()` | Empties the set |
| `del` | Deletes the entire set variable |
| `in` | Checks if an item exists in the set |

---

## 📌 Examples Used

```python
# Union
s1 = {1, 2, 5, 6}
s2 = {3, 5, 7}
print(s1.union(s2))  # {1, 2, 3, 5, 6, 7}

# Intersection
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.intersection(cities2))  # {'Tokyo', 'Madrid'}

# Add & Remove
cities.add("Helsinki")
cities.remove("Tokyo")

# Membership
if "Carla" in info:
    print("Carla is present.")
