# Magic Methods:- In python magic methods are also known as dunder methods(double underscore methods), are speacial methods that starts and end  with double undescores. these methods emables you to define the behaviour of objects for built-in operations, such as arithemtic operations, and more.
class Person:
    pass 

person = Person()
print(person)


#Basic methods 
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

student = Student("Manish",18)
print(student)#returns .Person object at 0x00000270241770E0>


#We used another magic method which is __str__ 
#that helps to return string representation of object 
class Student1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} , {self.age}"
student1 = Student1("Manish",18)
print(student1)# will return:-  Manish , 18
#best for returning value for user simple and readable


#__repr__ :-Used to return an official representation of an object, Meant for developers
class Student2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f"Student(name= {self.name} age= {self.age})"
student2=  Student2("Krish",20)
print(repr(student2))# return:- Student(name= Krish age= 20)
#best for returning value for programmer 


#Other magic methods 
#__len__ :- Return the length of an objects 
#__getitem__ :-Gets an item from a container 
#__setitem__ :-Sets an item in a container 