# 

import random

# Step 1: Set up the game
numbers = set(range(1, 11))  # Numbers 1 to 10

# Step 2: Player selects a number
my_choice = int(input("Pick a number between 1 and 10: "))

# Step 3: Game loop
while len(numbers) > 1:
    eaten = numbers.pop()
    print(f"Computer ate: {eaten}")
    
    if eaten == my_choice:
        print("💥 Oh no! Your number was eaten. You lose!")
        break
else:
    print("🎉 Congrats! Your number survived. You win!")
