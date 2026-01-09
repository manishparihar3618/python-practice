class Person:
    def __init__(self,name,age):
        self.name = name 
        self.__age = age

def get_name(Name):
    print(Name.name)

person = Person("Manish",18)
print(person.name)
# print(person.__age) #we cannot access this because its private variable and cannot be directly accessed outside the class 
get_name(person)
