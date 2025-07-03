#strings are immutable
#this will not convert or Change String into lower or upper case it will just create new string
a = "Manish"
print(len(a))
print(a.upper())
# all characters of Manish will be printed in upper case
print(a.lower())
# all characters of Manish will be printed in lower case 

#rstrip()
# this basically remove trailing characters ex:-
a ="Hello !!!"
print(a.rstrip("!"))
# so it will remove "!" 
# It !!!Hello !!!   it will only remove trailing character when we rstrip("!"") , output will be !!!Hello . 

#replace()
a = "!!!Manish!!!Manish!"
print(a.replace("Manish","Harry"))
#it will replace Manish by Harry

#split()
a = "!!!Manish !Manish"
print(a.split())
#it will split in ['!!!Manish!Manish!'] 

#capatilize() method turns only first character of the string to uppercase and rest all characters in lowecase . the string has no effect if the first character is already in uppercase
a = "introduction tO Python"
print(a.capitalize())

#center() this method aligns the string to the center as per the parameters given by user.
a = "Welcome to the console!!!"
print(a.center(50)) 
#it will basically shift it towards the center
print(len(a)) # in starting the lenght of a was 25
print(len(a.center(50))) # this added extra 25 
# we can see the differenece of lenght of both above lines

#count() this method gives how many times the given value has occured within the given string for ex-
a = "!!!Manish!!!,Manish,!!"
print(a.count("Manish")) # manish appeared 2 times in string a
print(a.count("!"))# number of times ! appeared in string a

#endswith() :- it gives us if string ends with given value .If yes then Return True , else return false .   
a = "!!!Manish!!!,Manish,!!"
print(a.endswith("!!")) #output will be True
#we can even cheak for a value in-between the strings by providing start and end index position. for ex-
a = "!!!Manish!!!,Manish,!!"
print(a.endswith("!!",4,22))# we will be cheaking endswith() between 4 to 18 if there is the value then it will print True else if not false
print(a.endswith("!!",4,18))