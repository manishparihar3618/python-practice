#Nested if else statment we can use if, if-else,elif statment inside others if statments as well.
num = 12
if (num < 0):
   print("Number is negative.")
elif (num > 0):
   print("Number is positive and")
   if (num <= 10):
     print("It is between 1-10")
   elif (num > 10 and num <= 20):
     print("It is between 11-20")
   else:
     print("It is greter than 20")
else:
   print("Number is zero")