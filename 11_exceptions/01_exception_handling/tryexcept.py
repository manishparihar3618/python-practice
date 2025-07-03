a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
 for i in range(1,11):
     print(f"{a} x {i} = {int(a)*i}")
except:
   print("Error occured")

print("End of program")

# What if we inserts string like manish in place of any number in input, Then it will give us error.  
# So we will be using try..except in line 4 and 5 there is chances of getting error becuse main logic and print statment is written in those lines so we will be writting try: before 4th line, and except Exception as e:
#  print(e) after 5th line 
# and using try...except if there is any error in line 4 or 5 then control will go after 5th line and next print statments will be printed.
