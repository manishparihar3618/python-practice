#Encapsulation:-Binding attributes(data) and methods(functions) together inside a class, and restricting direct access to some part.
#Helps to protect data from accidental modification and impoves security of code.

#access modifiers :- 
#(1) Public :- name, accesible everywhere 
#(2) Protected :- _name, accesible in class and subclass 
#(3) private :- __name, accesible only inside class



#Public members:-
class Student:
  def __init__ (self,name,age):
     self.name = name#This instance variables are known as public variable
     self.age = age #-----------||-------------


def get_name(student):#This is a fuction outside of the class Student but can access its variable
 print(student.name)

student = Student("Rahul",18)
print(student.name)
print(student.age)
get_name(student)
#Sometimes data in variable is important and should not be accesed outside its class so here we use private and protected variable


#Protected members:-
class Student1:
 def __init__(self):
     self._name1 = "RAVI"#protected variable(_name1)
class Teacher(Student1):
 def show(self):
    print(self._name1)#protected variable called inside the subclass
c =Teacher()
c.show()

     







# class Student:
#     __name = "Manish"
#Private attribute(__)
    
# obj = Student()
# print(obj.__name)# cannot be accesed by object and throws an error 



#Executing private attribute using constructor
class Student:
    __name="Manish"
    def __init__(self):
        print(self.__name)

obj = Student()#We used that private attribute but using cosntructor not directly



#private method or function with private attribute
class Student1:
    __name1 = "Manish"#declaration of private attribute 
    def  __init__(self):#constructor
        print(self.__name1)
        self.__displayinfo()#This line calls the private method
    def __displayinfo(self):#declaration of private methods 
        print("Welcome")

obj1 = Student1()#declaring a object




