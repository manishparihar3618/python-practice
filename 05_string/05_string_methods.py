# Demonstrates commonly used Python string methods

# Strings are immutable – operations return a new string
a = "Manish"
print(len(a))
print(a.upper())    # All uppercase
print(a.lower())    # All lowercase

# rstrip() – removes trailing characters
a = "Hello !!!"
print(a.rstrip("!"))

# replace() – replaces substrings
a = "!!!Manish!!!Manish!"
print(a.replace("Manish", "Harry"))

# split() – splits string into list
a = "!!!Manish !Manish"
print(a.split())

# capitalize() – capitalizes first character
a = "introduction tO Python"
print(a.capitalize())

# center() – aligns string to center
a = "Welcome to the console!!!"
print(a.center(50))  
print(len(a))             
print(len(a.center(50)))  

# count() – counts occurrences
a = "!!!Manish!!!,Manish,!!"
print(a.count("Manish"))  
print(a.count("!"))       

# endswith() – checks string end
print(a.endswith("!!"))  
print(a.endswith("!!", 4, 22))  
print(a.endswith("!!", 4, 18))  

# find() – returns index of first occurrence, or -1
a = "He's name is manish , he is very intelligent ."
print(a.find("is"))     
print(a.find("ishh"))   

# index() – like find() but raises error if not found
a = "He's name is anonomus , he is very intelligent ."
print(a.index("is"))    

# isalnum() – checks alphanumeric
print("Manishparihar".isalnum())
print("Manish9893parihar".isalnum())
print("Manish,parihar".isalnum())

# isalpha() – checks for only letters
print("Manish".isalpha())
print("Manish00".isalpha())

# islower() – checks lowercase
print("manishparihar".islower())
print("Manishparihar".islower())

# isprintable() – checks if all characters are printable
print("We wish you Happy Birthday".isprintable())
print("We wish you Happy Birthday\n".isprintable())

# isspace() – checks whitespace only
print("     ".isspace())     
print("	".isspace())         

# istitle() – checks if first letter of every word is uppercase
print("World Health Organisation".istitle())
print("World health organisation".istitle())

# isupper() – checks if all characters are uppercase
print("WORLD HEALTH ORGANIZATION".isupper())

# startswith() – checks if string starts with given value
print("World health organization".startswith("World"))

# swapcase() – swaps lowercase and uppercase
print("Python is a Interpreted Language".swapcase())

# title() – capitalizes first letter of each word
print("My name is manish parIhar i am a enginerring Student".title())