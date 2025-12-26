#Class:-
# It is blue print used to create Object.

#Object:-
# Object is a real world entities.

class person:
    name = "Harry"
    occupation = "software developer"
    networth = 10

a = person()
a.name = "Manish"
print(f"{a.name} is {a.occupation}")



class person:
    name = "Harry"
    occupation = "software developer"
    def info(self):#in any class we declare it will require a self argument execpt few
     print(f"{self.name} is a {self.occupation}")

a = person()
b = person()
c = person()
a.name = "Manish"
a.occupation = "Accountant"

b.name = "Shubham"
b.occupation ="HR"

a.info()
b.info()
c.info()#default value will print because in this 0bject no changes is made 