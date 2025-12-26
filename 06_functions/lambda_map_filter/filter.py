#filter:-
#The filter function filters a sequence of elements based on a given predicate(a function that return a boolean value) and return a new sequence containing only the elements that meet the predicate.
#Using filter with def
l =[1,5,6,4,3]
def filter_function(a):
 return a>4
newl= filter(filter_function,l)
print(list(newl))

#Using filter with Lambda function 
l =[1,5,6,4,3]
newlist=list(filter(lambda a:a>4,l))
print(newlist)