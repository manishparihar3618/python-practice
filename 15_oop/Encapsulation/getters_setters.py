# We can access the private methods or attributes inside a class but cannot access it outside the class 
#making data public can be unsafe anyone can modify it 
#getters and setters let you control how data is accessed or modified while keeping it private.
#data stays private but you open a safe way to read or write it.


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




#Encapsulation with getter and setter 
class Person:
 def __init__(self,name,age):
  self.__name=name
  self.__age = age

 def get_name(self):
  return self.__name

 def set_name(self,name):
  self.__name= name

 def get_age(self):
  return self.__age

 def set_age(self,age):
  if(age>0):
   self.__age = age
  else:
   print("Age cannot be negative")

person = Person("Manish",18)

#Access and modify private method using getter and setter

print(person.get_name())
print(person.get_age())

person.set_age(35)
print(person.get_age())

person.set_age(-5)
