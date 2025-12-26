# In python map,filter and reduce functions are built-in functions that allows you to apply a function to sequence of elements and return a new sequence. These functions are known as higher order functions, as they take other functions as arguments.
#ex
#without Map function
def cube(x):
   return x*x*x

l = [1,5,4,5,3]
newl = []
for item in l:
   newl.append(cube(item))

print(newl)


# Using Map function
l = [1,5,4,5,3]
newlist = list(map(cube,l))
print(newlist)

#Using Map function with lambda function 
l = [1,2,3,4,5]
newList1= list(map(lambda x:x*x*x, l))
print(newList1)