# String length and slicing examples

names = "Manish,Parihar"
print(len(names))  # Total characters in the string

fruit = "mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word")

# String slicing
print(fruit[0:3])   # Output: man
print(fruit[:3])    # Same as fruit[0:3]
print(fruit[1:4])   # Output: ang
print(fruit[:])     # Output: mango (entire string)

# Negative indexing
print(fruit[0:-3])      # Output: ma
print(fruit[-1:-3])     # Output: '' (invalid range)
print(fruit[-3:-1])     # Output: ng

# Index map for 'mango'
#   m   a   n   g   o
#   0   1   2   3   4
#  -5  -4  -3  -2  -1
names = "Manish,Parihar"

# Slicing from index 0 to 5 (end index 6 is not included)
print(names[0:6])  # Output: Manish

# Note: The comma (,) at index 6 is not printed because slicing excludes the end index.
