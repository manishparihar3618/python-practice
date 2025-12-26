class Person:
 name = "Harry"
 occ = "Developer"

 def info(self):
  print(f"{self.name} is a {self.occ}")

a = Person()
a.name="Divya"
a.occ ="HR"
a.info()


#Constructor
#After declaring constructor using def __init__(self) whenever we will create a object it will call the constructor
class Person1:
 def __init__(self):
  print("Calling")

a = Person1()
b = Person1()
#For every object we create it will call constructor and will print Calling


class Person2:
 
 def __init__(self,n,o):
  self.name = n
  self.occ = o

 def info(self):
  print(f"{self.name} is a {self.occ} ")


a = Person2("Manish","Developer")
b = Person2("Divya","HR")
a.info()
b.info()

#Okay in def __init__ we have 3 arguments one is self which is will be passed when we will declare a object in this class and next two arguments n and o will take arguments from objects

#Types of constructors     (1) Parameterized:- when we pass arguments with self                      (2) Default:- When we pass only self 