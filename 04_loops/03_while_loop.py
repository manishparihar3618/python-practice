# while_loops.py

# (1) Basic while loop
i = 0
while i < 5:
    print(i)
    i = i + 1  # Increments i until condition becomes False

# (2) while loop with user input
i = 0
while i <= 24:
    i = int(input("Enter the number: "))
    print(i)

print("Done with the loop")
# This loop will continue until a number greater than 24 is entered.

# (3) while loop with else
count = 5
while count > 0:
    print(count)
    count -= 1
else:
    print("I am inside else")
# 'else' runs only when the loop completes normally (no break)
