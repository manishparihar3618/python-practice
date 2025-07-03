#String formatting in python:-
# String formatting can be done in python using the formate method.
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Manish"
print(letter.format(name,country))
#This method will be putting both name and country in thier specific places
  
print(letter.format(country,name))
#This will give output as 
#Hey my name is India and I am from Manish

#Before python 3.6 we used to give arguments to brackets EX-
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Manish"
print(letter.format(country,name))
#But that was very inconvenient method we can get confused if thier are 4-5 arguments
#To overcome that problem The concept of f-string was introduced in Python.
country = "India"
name = "Manish"
print(f"Hey my name is {name} and I am from {country}")

# another example:-
#Without using f-string:-
txt ="For only {price:.2f}  dollars!"
print(txt.format(price = 49.09999))
#Output:-For only 49.10  dollars!
#We used :.2f so it will only print 2 digits after 49
#Using f-string
price = 49.09999
print(f"For only {price:.2f}  dollars!")

# another example:-
val ='Geeks'
print(f"{val}for{val} is a portal for {val}.")
name = 'Tushar'
age = 23 
print(f"Hello, My name is {name} and I'm {age} years old.")
#Output:- Hello, My name is Tushar and I'm 23 years old.
#In the above code, we have used the f-string to format the string. It evaluates at rumtime; we can put all valid python expressions in them.
#We can use it in single statement as well.
print(f"{2*30}")
#Output:- 60

print(f"Hey my name is {name} and I am from {country}")
#If I want to print it as it is:-
print(f"Hey my name is {{name}} and I am from {{country}}")
#Use