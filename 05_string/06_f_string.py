# Demonstrates string formatting in Python using format() and f-strings

# Using format() method
letter = "Hey my name is {} and I am from {}"
name = "Manish"
country = "India"
print(letter.format(name, country))  # Inserts in order
print(letter.format(country, name))  # Swaps order

# Positional formatting
letter = "Hey my name is {1} and I am from {0}"
print(letter.format(country, name))  # Uses index to reorder

# f-strings (Python 3.6+)
print(f"Hey my name is {name} and I am from {country}")

# Formatting float to 2 decimal places
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49.09999))

# f-string version
price = 49.09999
print(f"For only {price:.2f} dollars!")

# f-string with multiple values
val = "Geeks"
print(f"{val}for{val} is a portal for {val}.")

# f-string with expressions
name = "Tushar"
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")
print(f"{2 * 30}")  # Expression inside f-string

# Escaping braces in f-strings
print(f"Hey my name is {{name}} and I am from {{country}}")  # Prints placeholders literally
