#Manipulating tuples
#Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back in tuple.
countries = ("Spain", "Italy", "India", "England", "Germany")# Tuple
temp = list(countries)#Converted into a List.
temp.append("Russia")#Added Russia at end using append method in list.
temp.pop(3) #Removed England(index 3) using pop method in list.
temp[2] = "Finland" #Changed India()index 2 with Finland.
countries = tuple(temp)#Converted back into a Tuple.
print(countries)


#However we can directly concatenate two tuples without converting them to list.
countries = ("Pakistan", "Afghanistan", "Bangladesh", "Srilanka")
countries2 =("India", "China", "Vietnam" )
SouthEastAsia = countries + countries2
print(SouthEastAsia)

#Methods
#Tuple Methods
#As tuple is immutable type of collection of elements it have limited built in methods. They are explained below

#(1)Count method:-
#returns number of times the given element appears in the tuple.
Tuple1 = (0,1,2,3,2,1,3,2,3)
res =Tuple1.count(3)
print("Count of 3 in Tuple1 is :", res)

#(2)Index Method:-
#returns first occurence of the given element from the tuple.
Tuple1 = (0,1,2,3,2,3,1,3,2)
res = Tuple1.index(3)
print("Index of first Occurence of 3 is:-",res)

res = Tuple1.index(3, 4, 8)#it will be doing slicing means between index 4 to 8 it will cheak the first occurence of 3 
print("Index of first Occurence of 3 between index 4 to 8 is:-",res)


#(3) Length Method:-
Tuple1 = (0,1,2,3,2,3,1,3,2)
print("Length of Tuple is:-",len(Tuple1))