# Variable declarations with different data types
a = 123                # Integer
a1 = 9                 # Integer
b = True               # Boolean
c = "Manish"           # String
d = None               # NoneType (represents null)
e = complex(8, 2)      # Complex number
f = 1.000008           # Float

# Output of variables
print(a)  
print(b)
print(a + a1) 
print(e)
print(f)
print(a + f)

# Displaying the type of each variable
print("The type of a is:", type(a)) 
print("The type of b is:", type(b))
print("The type of c is:", type(c))
print("The type of d is:", type(d))
print("The type of e is:", type(e))
print("The type of f is:", type(f))

# Note:
# You cannot perform arithmetic operations between incompatible data types
# For example, adding a string and an integer will cause an error:
# a = "Manish"
# b = 9
# print(a + b)  # ❌ TypeError: can only concatenate str (not "int") to str
