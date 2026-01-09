class Student:
 def __init__(self,name,marks):
    self.__name = name
    self.__marks = marks
 def get_name(self):
    return self.__name
 def set_name(self,name):
    self.__name = name
 def get_marks(self):
    return self.__marks
 def set_marks(self,marks):
    if(0<= marks <=100):
       self.__marks = marks
    else:
       print("Invalid")

s = Student("Manish",95)
print(s.get_name())
print(s.get_marks())
 
s.set_marks(110)