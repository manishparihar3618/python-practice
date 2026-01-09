# Inheritance 
# It is fundamental concept of oop which allows class to inherit attributes and properties from another class.

# Single Inheritance
class Car:
    def __init__ (self,windows,doors,enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype

    def drive(self):
        print(f"Person is driving a {self.enginetype} car")


car1 =Car(4,4,"Petrol")
car1.drive()

class Tesla(Car):
 def __init__(self,windows,doors,enginetype,is_selfdriving):
  super().__init__(windows,doors,enginetype)
  self.is_selfdriving = is_selfdriving

 def selfdriving(self):
    print(f"Does this Tesla car support Self driving: {self.is_selfdriving}")

teslacar = Tesla(2,2,"EV",True)
teslacar.selfdriving()
teslacar.drive()


#Multiple Inheritance:- When a class inherits from more then one base class 
class Animal:
   def __init__(self,name,ears,nose,legs):
      self.name = name 
      self.ears = ears
      self.nose = nose
      self.legs = legs
   def numberoflegs(self):
     print(f"{self.name} have {self.legs} legs")

class Dog():
   def __init__(self,sound):
      self.sound = sound

   def vocalsound(self):
      print(f"Dog {self.sound}")
    

class Puppy(Animal,Dog):
   def __init__(self,name,ears,nose,legs,sound):
      Animal.__init__(self,name,ears,nose,legs)
      Dog.__init__(self,sound)

   def show(self):
      print("Method of Puppy class")


puppy1 = Puppy("Moti",2,1,4,"Barks")
puppy1.show()
puppy1.numberoflegs()
puppy1.vocalsound()