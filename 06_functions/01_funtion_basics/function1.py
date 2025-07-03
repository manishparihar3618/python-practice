#  function is a block of code that perform a specific task whenever it is called. In bigger programms we have larger amount of code , it is advisible to create or use existing functions that makes the program flow organized and neat. 

# a = 9
# b = 8
# gmean = (a*b)/(a+b)
# print(gmean)
# c = 12
# d = 5
# gmean = (c*d)/(c+d)
# print(gmean)


# We want to calculate the geometric mean of different pairs of numbers.
# In the earlier code, we repeated the same logic for each pair.
# To avoid writing the same formula again and again,
# we define a function named 'gmean' that takes two numbers as input,
# calculates the geometric mean using the formula: (a * b) / (a + b),
# and returns the result. We can now reuse this function for any number of pairs.
def calculateGmean(a , b):
    mean = (a*b)/(a+b)
    print(mean)
def isgreater(a , b):
    if(a > b):
        print("first Number is Greater")
    else:
        print("Second Number is Greater")
def islesser(a , b):
    pass #we will be writing its body later so we will be writing pass 
a = 9
b = 8
isgreater(a , b)

calculateGmean(a , b)
c = 12
d = 5
isgreater(c , d)
calculateGmean(c , d)

# User-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.
#Above Programm is example of User-defined
#Syntax:-
def function_name(parameters):
    pass