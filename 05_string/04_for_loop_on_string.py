a = '''He said,
how are you
I replied nice
Then he said goodbye'''

print("Let's use a for loop:\n")

# Looping through each character in the string
for character in a:
    print(character)

# This prints each character of the string 'a' one by one



#Cheak Palindrome Number
a = input("Enter a number: ")
rev = ""
for i in range(len(str(a))-1,-1,-1):
    rev = rev + str(a)[i]
    
if a == rev:
        print("Its a palindrome")
else:
    print("Its not a palindrome")