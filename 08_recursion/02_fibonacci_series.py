def fibonacci(n):
    if n == 0 or n == 1:
      return 1
    else:
      return fibonacci(n - 1) + fibonacci(n - 2)
    
n = int(input("Enter the number : "))
print("Fibonacci at position " ,n, " is:", fibonacci(n))
