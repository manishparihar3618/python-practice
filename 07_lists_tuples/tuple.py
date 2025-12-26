# Python Tuples:- Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brakets(). Tuples are unchangeable meaning we can not alter them after creation.
tup = (1,5)
print(type(tup)) # tuple
tup = (1,5,3)
print(type(tup)) # tuple
tup = (1)
print(type(tup)) # int
tup = (1,)
print(type(tup),tup) # tuple

tup = (1,2,76,342,32,"green",True)
print(tup[0])
print(tup[1])#positive indexing example
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
print(tup[6])
print(tup[-1])#negative indexing example
print(tup[-2])

if 342 in tup:
 print("Yes it is present in this tuple ")
else:
 print("No its not there")

tup2 =tup[1:4]#slicing 
print(tup2)

#Conversion of negative indexes into positive indexes
tup = (1,2,3,4,5,6,7,8,9)
print(tup[:-3])
print(tup[:6])#length of tup - 6