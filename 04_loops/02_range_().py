# for_loop.py

# Basic for loop example
for i in range(5):
    print(i)

# --- RANGE USAGE EXAMPLES ---

# Example 1: range(9)
for k in range(9):
    print(k)        # prints 0 to 8
    print(k + 1)    # prints 1 to 9

# Example 2: range(1, 9)
for k in range(1, 9):
    print(k)        # prints 1 to 8
    print(k + 1)    # prints 2 to 9

# Example 3: range(1, 100)
for k in range(1, 100):
    print(k)        # prints 1 to 99

# Example 4: range(1, 15, 3)
for k in range(1, 15, 3):
    print(k)        # prints 1, 4, 7, 10, 13

# Example 5: range(1, 9, 3)
for k in range(1, 9, 3):
    print(k + 1)    # prints 2, 5, 8
