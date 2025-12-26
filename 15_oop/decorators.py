# Decorators:- A decorator is a function that takes another function as input, adds some extra behavior before or after it runs, and returns the modified function — without changing the original function’s code.


def routine(fx):
    def wrapper():
        print("Good morning")
        fx()
        print("Have a nice day")
    return wrapper

@routine
def work_doing_Rn():
    print("I am having my breakfast")

@routine
def workout():
    print("Doing Exersice")

work_doing_Rn()
workout()





def problem(fx):
    def wrapper1(*args,**kwargs):
        print("Solution of our problemis given below")
        fx(*args,**kwargs)
        print("Solution of our problem is given above")
    return wrapper1

@problem
def add(a,b):
    print(a+b)

add(1,2),







def checker(fx):
    def wrapper2():
        a = int(input("Enter a number: "))  
        if a < 0:
            print("It's not a positive number")
        else:
            print("It's a positive number")
        fx(a)
    return wrapper2

@checker
def number(n):
    print(f"The number entered is: {n}")

number()
