#Encapsulation:-Binding attributes(data) and methods(functions) together inside a class, and restricting direct access to some part.


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
