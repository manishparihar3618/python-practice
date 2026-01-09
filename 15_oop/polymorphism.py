#It is concept of OOP that allows objects of different classes to be treated as object of a common superclass. It provides a way to perform a single action in different forms. Polymorphism is typically achieved through method overriding and interfaces.

#Method overriding:- it allows child class to provide a specific implementation of a method that is already defined in parent class 

#Base or Parent class
class Animal:
  def speak(self):
    return "Sound of a Animal"
#Derived or Child class 1  
class Dog(Animal):
  def speak(self):
    return "Woof"
#Derived or Child class 2
class Cat(Animal):
  def speak(self):
    return "Meow"

#Function that demonstrate polymorphism
def animal_speak(animal):#public method 
  print(animal.speak())

dog = Dog()
cat = Cat()
print(dog.speak())#executes method of child class 1 which is Dog class
print(cat.speak())
#This shows method overriding where speak method is overrideen in both child classes 

animal_speak(dog)#So we give dog object as parameter to the animal_speak function and it prints dog.speak() there 


#Polymorphism with functions and methods 
class Shape:
  def area(self):
    return "Area"

class Rectangle(Shape):
  def __init__(self,length,breath):
    self.length = length
    self.breath = breath
  def area(self):
    print(f"The area of rectangel will be: ",self.length * self.breath)

class Circle(Shape):
  def __init__(self,radius):
    self.radius= radius
  def area(self):
    print(f"The area of circle is: ",3.14 * self.radius * self.radius)

def find_area(shape):
  print(shape.area())

Rectangle1 = Rectangle(5,4)
Circle1 = Circle(3)

print(Rectangle1.area())
print(Circle1.area())

find_area(Rectangle1)
find_area(Circle1)

  

#As we know polymorphism can be also achived through interfaces.
#In Python we say interfaces as Abstract Base class 
#Abstract Base class
from abc import ABC,abstractmethod

class Vehicle(ABC):
  @abstractmethod
  def start_engine(self):
    pass 
  
class Car(Vehicle):
  def start_engine(self):
    return "Car engine started"
  
class Bike(Vehicle):
  def start_engine(self):
    return "Bike engine started"
  
def start_vehicle(vehicle):
 print(vehicle.start_engine())
  
car = Car()
bike = Bike()

print(car.start_engine())
print(bike.start_engine())
start_vehicle(car)
start_vehicle(bike)





class shape:
  def area(self)
    