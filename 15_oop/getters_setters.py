# We can access the private methods or attributes inside a class but cannot access it outside the class 
#making data public can be unsafe anyone can modify it 
#getters and setters let you control how data is accessed or modified while keeping it private.
#data stays private but younopen a safe way to read or write it.


#Getters
class Student1:
 def __init__(self):
  self.__name1 = "Manish"#private attribute

#Getter method
 def get_name(self):
  return self.__name1
 
#---Outside the class---
obj =Student1()
print(obj.get_name())#accessing via getters




#Using getter and setter 
# setter are used to modify the private value safely
class Student2:
 def __init__(self):
   self.__name1 ="Manish"

 def get_name1(self):
  return self.__name1
 
 def set_name1(self,new_name):
  if len(new_name)>0:
    self.__name1 = new_name
  else:
   print("Name cannot be empty!")


   obj = Student2()
   print("Before update:",obj.get_name1())

   obj.set_name1("Rohit")
   print("After update:",obj.get_name1())