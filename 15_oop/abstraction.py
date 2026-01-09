#Abstraction :-It is the concept of hiding the complex implementation details and showing only the neccesory features of an object. This helps in reducing programming complexity and efforts
#Real world example:- Lets take A washing machine as an Object where when we press the button it starts rotating and cloths gets washed so the button is feature of Object which is washing machine. but we dont know the internal complex process that will happen inside the washing machine after presssing that button. 
from abc import ABC,abstractmethod

#Abstract base class
class Vehicle(ABC):
    def drive(self):
        print("The vehicle is used for driving")

    @abstractmethod
    def start_engine(self):
     pass

class Car(Vehicle):
  def start_engine(self):
   print("Car engine started ")
   
def operate_vehicle(vehicle):
  vehicle.start_engine()
  vehicle.drive()


car = Car()
operate_vehicle(car)

