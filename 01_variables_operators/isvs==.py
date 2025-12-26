a = 4
b = "4"
print(a is b)#exact location in memory 
print(a == b)#value 


Manish= "Iphone",15
Harry= "Iphone",15
print(Manish is Harry)
print(Manish == Harry)


a1 = [1,2,43]
b1 = [1,2,43]
print(a1 is b1)#False 
print(a1 == b1)#True 
# both a and b have same value but are two different things 


a1 = 3
b1 = 3
print(a1 is b1)#True
print(a1 == b1)#True
#So in python when we create a constant like we created 3 in above case so in memory location it is created one time in memory location and python knows it is constant so it will not be changed. So python will not waste another memory location and it will not assign new memory location to another constant 3. so that why saying a is b will be true because both have same memory location. 
#Python do not make memory for small integers from -5 to 256 and small strings.


a2 = "harry"
b2 = "harry"
print(a2 is b2)
print(a2 == b2)


a3 = (1,2,3)
b3 = (1,2,3)
print(a3 is b3)
print(a3 == b3)


#Example from my side 
a4 = 2
b4 = 2+0
print(a4 is b4)
print(a4 == b4)



# == compares the values of both objects or variables 
# is cheaks for memory location 