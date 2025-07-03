# do_while_simulation.py

# Simulating a do-while loop in Python
# A do-while loop runs the code block at least once, regardless of the condition

i = 0
while True:
    print(i)
    i = i + 1
    if i % 100 == 0:
        break  # exit the loop when i is divisible by 100
