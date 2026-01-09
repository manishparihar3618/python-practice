#Our code shows we have used protected variable which is accessed in subclass 


class Person:
    def __init__(self,name):
        self._name = name #portected variable

class Person2(Person):
    def __init__(self,name,age):
     super().__init__(name)
     self.age = age

    
person = Person2("Manish",18)
print(person._name)


