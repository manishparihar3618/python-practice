#istitle():- This method return True only if the first letter of each word of the string is capatalized, else it return false.
a = "World Health Organisation"
b = "World health organisation"
print(a.istitle())#first letter of all words are in capital.
print(b.istitle())#first letter of all words in string are not in capital.

#isupper():- this method return True if all characters in string are upper case, else it return false.
a = "WORLD HEALTH ORGANIZATION"
print(a.isupper()) # Output will be True 

#startswith():- This Method returns True if the string starts with a given value. else it returns false.
a = "World health orgranization"
print(a.startswith("World"))



#swapcase():-This method changes the characters casing of string. upper case are converted to lower case and lower case are converted to upper case.
a = "Python is a Interpreted Language"
print(a.swapcase())

#title():-This method convert first letter of each word in capital letter within the string. and other letter into lower case.
a = "My name is manish parIhar i am a enginerring Student" 
print(a.title())