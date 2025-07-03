#(3)Keyword Arguments:-
#We can provide arguments with key=value,this way the interpreter recognizes the arguments by the parameters name. Hence, the order in which the arguments are passed does not matter.
def average(a=9,b=1):
  print("The average is", (a+b)/2)

average(b=9,a=21)
#order do not matter in keyword argument


# (4)Required Arguments:-
#In case we don't pass the arguments with a key=value syntax,then it is necessory to pass the arguments in correct positional order and the numbers of arguments passed should match with actual functions defination.
def average(a,b,c=1):
  print("The average is ",(a+b+c)/2)

average(5,6)
#the value of a,b is required to run the code

#(5)Variable-length Arguments:
#Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.
#sometimes we don't know how many times we have pass value to function in that case we use it.
def average(*numbers):
  #print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  print("Average is:",sum / len(numbers)) 

average(5,6,7)
#*numbers/*args/*values
#explanation of above programn
# *numbers means: You can pass any number of values to the function, and all of them will be stored together in a tuple called numbers.
#we used forloop to sum 5+6+7
#logic was sum/len(numbers)

def name(**name):
  print("Hello,",name["fname"],name["mname"], name["lname"])

name(mname="Buchanan",lname="Barnes",fname="James")
