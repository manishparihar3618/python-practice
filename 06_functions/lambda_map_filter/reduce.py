#Reduce function:-
#The reduce function is a higher-order function that applies a function to a sequence and return a single value. It is a part of the functools module in Python. 
#Syntex :- reduce(function, iterable)

from functools import reduce

numbers = [1,2,3,4,5]

def mysum(x,y):
    return x+y
sum = reduce(mysum,    numbers)

print(sum)
# List = [1, 2, 3, 4, 5]First call → mysum(1, 2) = 3
# Next call → mysum(3, 3) = 6
# Next call → mysum(6, 4) = 10
#Next call → mysum(10, 5) = 15
#Final result = 15List = [1, 2, 3, 4, 5]
#First call → mysum(1, 2) = 3
#Next call → mysum(3, 3) = 6
#Next call → mysum(6, 4) = 10
#Next call → mysum(10, 5) = 15
#Final result = 15