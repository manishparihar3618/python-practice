# Python Lists:-
#Lists are collection of data items.
#They store multiple items in a single variable
#List items are seprated by commas and enclosed within square brackets[].
#List are changeable meaning we can alter them after creation.
marks =[3,4,5,]
print(marks)
print(type(marks))
print(marks[0])#concept of indexing works same in list, 0 will be printing first element from given list which is 3.
print(marks[1])
print(marks[2])
#we can even add diff types of datatypes in same list for example 
marks = [3,4,5,"string",True]
# Positive indexing:- 
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(len(marks))
#We have already learned concept of accesing items from list, in above program
# Negative indexing:- 
print("Negative indexing",marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])
#marks[-3] is basically 5-3=marks[2]
#Cheak whether an item is present in list?
print("Conditional concept in list")
if 6 in marks:
    print("Yes")
else:
    print("No")

if "stri" in "string":
    print("yes")

print(marks)
print(marks[1:])
print(marks[:])
print(marks[:5])
print(marks[1:-1])
print(marks[1:4])#converted above 1:-1 into positive indexing using 1:5-1 = 1:4 
#Jump index
print(marks[1:4:2])
# it will first print 4 whose index is 1 and then will jump 1 index then it will print 'string'

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)