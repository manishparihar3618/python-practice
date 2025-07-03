##find():- searches for the first occurance of the given value and returns the index where it it present . if given value is absent from string then -1.
a = "He's name is manish , he is very intelligent ."
print(a.find("is")) # output will be 10 the indexing of first occurence of "is". after 0,1,2,3,4,5,6,7,8,9 the 10 indexing will be of i of "is"
print(a.find("ishh")) # it will give -1 because there is no occurence of ishh .

## index() :-it searches for the first occurence of the given value and return the index where it it present. if given value is absent from the string then it raises an exception . 
a = "He's name is anonomus , he is very intelligent ."
print(a.index("is")) # it will be giving same output like find which will be 10 .
# a = "He's name is anonomus , he is very intelligent ."
# print(a.index("ishh")) # it will be giving error because there is not occurence of ishh, raise exception.

##isalnum():-this method return true only if the entire string consist of A-z,a-z,0-9 or we can say alphanumeric . if an character or punctuations are present, then it returns False.
a = "Manishparihar"
print(a.isalnum()) #output is True because string consist alphanuemrics.
a = "Manish9893parihar"
print(a.isalnum()) # output is True
a = "Manish,parihar"
print(a.isalnum()) #output is false because it consist , which is not alphanumeric. 

##isalpha():-this method returns True only if the entire string only consists of A-Z,a-z. if any other characters or punctuations or numbers(0-9) are present, then it returns False.
a = "Manish"
b = "Manish00" 
print(a.isalpha()) #output is True Because it consist A-Z,a-z only.
print(b.isalpha()) #output is False Because it consist (0-9).

## islower():- this method gives True if all characters are in lower case,else it return false.
a = "manishparihar" 
print(a.islower()) #output is True because all characters are in lowercase
a = "Manishparihar" 
print(a.islower()) #output is False

## isprintable():- This method gives True if all the values within the given string are printable, if not, the returns False.
a = "We wish you Happy Birthday" 
print(a.isprintable())#output will be True because all are printable values in string
a = "we wish you Happy Birthday\n" 
print(a.isprintable())#output will be false because \n is not a printable value in string

#isspace():- This method returns True only if string contains white spaces, else return False
a = "         "#spacebar
print(a.isspace())
b = "           "#tab
print(b.isspace())
#output of both a and b will be True.
  