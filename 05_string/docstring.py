#Docstrings:- 
# Python docstrings are the string literals that appears right after the defination of a function, method, class, or module.
def square(n):
 '''Takes in a number n, returns the square of n'''
 print(n**2)
square(5)
print(square.__doc__)

#Python comments:- Notes in the code for developers only. Ignored by the Python interpreter. Used to explain why or how something works.
#Python Docstrings:- Special strings used to document functions, classes, or modules.Can be accessed using the .__doc__ attribute.Written using triple quotes """ ... """ or ''' ... '''
#Python Doc attribute:- The __doc__ attribute holds the string defined immediately after the def, class, or module keyword, written in triple quotes.

