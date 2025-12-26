# for_else_loop.py

# Example 1: Normal for loop with else
for i in range(5):
    print(i)
else:
    print("Sorry no i")  # This runs because the loop finished without break


# Example 2: For loop with break — else will NOT run
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("Sorry no i")  # This does NOT run because break was hit


# Example 3: While loop with else
i = 0
while i < 7:
    print(i)
    i = i + 1
else:
    print("Sorry no i")  # This runs because while loop finished normally
