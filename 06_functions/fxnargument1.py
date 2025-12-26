#Function Arguments :-
#Their are 5 types of arguments we can provide in a function
 
#(1)Positional Argument:-
def average(a,b):
  print("The average is", (a+b)/2)

average(4,6)
#it will be assuming a=4 and b=6 


#(2)Default Argument :- We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in a function call for that Argument.

def average(a=9,b=1):
  print("The average is", (a+b)/2)

average()
#it will run and will give output 5 
#it will be assumme value of a=9 and b=1

def average(a=9,b=1):
  print("The average is", (a+b)/2)

average(1,5)
#it will run and will give output 3. It will be ignoring a=9 and b=1 completly

def average(a=9,b=1):
  print("The average is", (a+b)/2)

average(5)
#it will be taking value of a=5 and b=1

def average(a=9,b=1):
  print("The average is", (a+b)/2)

average(b=9)
#it will be taking value of a=9 and b=9

def name(fname,mname ="Jhon",lname="Whatson"):
  print("Hello,",fname,mname,lname)
name("Amy","agarwal")