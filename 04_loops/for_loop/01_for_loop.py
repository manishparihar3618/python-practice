# Demonstration of for loop with a string
name = 'Manish'

for i in name:
    print(i)
    if i == "n":
        print("This is something special")

# ✅ To loop over digits in a number, convert it to a string first:
a = 254
for digit in str(a):
    print(digit)

# Another valid example
word = 'manish'
for char in word:
    print(char)
    if char == "n":
        print("OK!")

colors =["Red","Green","Blue","Yellow"]
for color in colors:
 print(color)#this code will be giving output each red green blue yellow in different lines 
 for i in color:
    print(i)# again iterated it 