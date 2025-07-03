# factorial(5) =5*4*3*2*1
# factorial(4) =4*3*2*1
# factorial(0) =0
# factorial(n) = n * factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))
print(factorial(4))
print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1
#When we will be calculating factorial(1)
# this time the if condition will be true and it will print 1  

#Fibonacci number:-
# f0 = 1
# f1 = 1
# f2 = f1 + f0
# fn =f(n-1)+f(n-2)