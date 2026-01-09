class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self,name,age,id):
     self.id = id
     super().__init__(name,age)

    def show(self):
       print(f"Employee name is {self.name} his age is {self.age} and his id is {self.id}")

Employee1 = Employee("Manish",18,44436) 
Employee1.show()