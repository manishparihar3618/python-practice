#lambda function:-
# a lambda function is a small anonymous function without a name. It is defined using lambda keyword and has the following syntex:
#lambda arguments: expression

#Using def to declare function and use it 
def double(x):
    return x*2
print(double(5))

#Use of lambda function 
double2 = lambda x: x*2
print(double2(5))
#benifits of using lambda functions are:-
#(a) No need to worry about indentation       (b) No need to type def and return and reduce use of lines in code 
#another ex:-
#Using def
def cube(x):
    return x*x*x
print(cube(3))
#Using lambda function
cube2 = lambda x: x*x*x
print(cube2(5)) 

#another example:-
average = lambda x,y,z: (x+y+z)/3
print(average(2,4,6))

#passing function to function
def apply(fx,value):
    return 6 + fx(value)

print(apply(cube,2))
#cube will go to fx and 2 will go to value so cube of 2 then + 6
# arguments in concept of function is not always numbers or strings it can be functions
#lambda function
apply1 = lambda fx,value: 6+ fx(value)
print(apply1(cube,3))
