# Task: Take a password as input and check if it is strong, moderate, or weak.
# Strong: At least 8 characters, has uppercase, lowercase, digit.
# Moderate: At least 6 characters, has two of the above.
# Weak: Anything else.
# passport cheaker
a = input("Enter the password :")
print("Number of digits in our password is :",len(a))
if(len(a) >= 8):
    print("Your Password Level is Strong")
elif(6 <=len(a)< 8):
    print("Your Password Level is Moderate")
else:
    print("Your Password Level is Low")