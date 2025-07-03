# def sumresult(a,b):
#      add= a+b
#      print("The summation is: ", add)
# a=12
# b=13
# sumresult(a,b)

# def iseven(a):
#     num = (a%2==0)
#     if(num):
#      print("The number is Even:")
#     else:
#        print("The number is odd")
# a = 7
# iseven(a)

# def greet(name):
#     print("Hello,",name +"!")
# greet(input("Write name of person you want to greet: "))

# def square(n):
#     num = n**2
#     print(num)
# n = 4
# square(n)

# def future_work():
#     pass

def greet(name):
    print("Hello",name)

greet("manish")


def multiply(a,b):
    into=a*b
    print(into)

multiply(4,5)

def info(name,age=18):
    print("Name:-",name)
    print("Age:-",age)

info("Manish")

def subtract(a=10, b=5):
       print('Result:', a - b)
subtract()
subtract(20)
subtract(b=2)


def area(length,width=5):
    areaofrectangle=length*width
    print("Area of Reactangle is:-",areaofrectangle)

area(7)
area(7,6)



def area(length=3,width=5):
    areaofreactangle=length*width
    print("Area of Reactangle is:-",areaofreactangle)

area()
area(1,)
area(4,5,)





def describe(city, country):
       print(f"{city} is in {country}")
describe("Paris", "France")
describe(country="India", city="Delhi")
# f stands for f-string


# def display(name, age):
        # print(name, age)
   
# display("Manish")
#will cause an error











