# short_hand_if_else.py

# Shorthand If and If-Else Examples

# Example 1: Simple if statement (regular and shorthand)
num = 4

# Regular if
if num % 2 == 0:
    print("It is even")

# Shorthand if (one-liner)
if num % 2 == 0: print("It is even")

# Example 2: if-else statement (regular and shorthand)
# Regular if-else
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Shorthand if-else (one-liner)
print("Even") if num % 2 == 0 else print("Odd")

# Example 3: Multiple conditions in shorthand
a = 330
b = 3303

# Print based on comparison
print("A") if a > b else print("=") if a == b else print("B")

# Example 4: Assigning values using shorthand if-else
c = 9 if a > b else 0
print(c)