names = "Manish,Parihar"
print(len(names))
# we can determine the length of any string
fruit = "mango"
len1 = len(fruit)
print("Mango is a",len1,"letter world" )
#easy cases of lenght of string
#now we will discuss if we have to print specific letters of mango
#we will use [0:n-1] 
fruit = "mango"
len1 = len(fruit)
print(fruit[0:3])#even if we only write[:4] python will consider it 0
# start from zero end will be n-1 which is 3-1 is 2 so 0:2 will be printed
print(fruit[:3])
print(fruit[1:4])
print(fruit[:])# python will apply 0 to len(fruit)
print(fruit[0:-3])#it will read it like 0 to 4-3 which will be 4-3 = 1 so ans will be [0:1]
print(fruit[-1:-3])# it will read it like [len(fruit)-1:len(fruit)-3]
#which will be 5-1:5-3   
# 4:2 which does no make any sence so out will be nothing 
print(fruit[-3:-1])# i will be [len(fruit)-3:len(fruit)-1] which will be 5-3:5-1 which is 2:4.and we know that python will start reading from 2 and th last will be n-1 which is 4-1 is 3 so 2:3 that is ng
#rule of indexing Mango
#                 01234
#               -5-4-3-2-1