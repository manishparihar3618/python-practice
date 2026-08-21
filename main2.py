#Test 1 (29-03-2026) 20 min 3.55 to 4.20



# Que 1: List is a mutable and changable collection of data and numbers 
# syntex: List = [1,2,3,4,5] we can perform direct operations on this 
# Tuple is immutable 
# syntex : tup = (1,2,3,4,5) we need to create it as list then perform opeartion and then make is tuple again


# Que 2:  what does this output?
# Python
# a = [1,2,3]
# print(a[::-1])
# Ans: dont know



#Que 3 Difference between == and =
# == it is a comparison operator example a == b means will written true if correct in if else 
#  = it assigns value to variable like a = 10 means 10 value is assigned to a 


#Que 4 What is a dictionary?
# A collection of keys and values where we can access the desired value with help of its key or we can also access only values or keys syntex A = {keys,'value'}


#Que 5 What is None in Python?
# None is usually like a output we get in python like True and false comes in None type when we do this 
#  Ex: a = True , print(type(a)) it writtens None 


# Section B 3 mark
#Que 6 What is a function? Why use it?
# function is a reusbale block of code in python used to write a maintable and resuable program, we define it by def keyword and write our main logic in it whenever we require to use the logic wiht diffefent attributes we call that fxn 


#Que 7 Difference between for loop and while loop
# loop is basically 
#loop = 3
# for i in loop:
# print(i)
# While loop is
# a = 5
# while (a>5):
#  print(a)
#  i forgot syntex and dont know the differece only know that loop have range fxn Where we can crerate a loop like range(2,6)



#Que 8 What is recursion?
# recursion is a concept of data structure where we write a fucntion to solve our problems which requires us to recall the fucntion again again untill the end condition is reached ex: fibbonaci factorial  



#Que 9: What is exception handling?
# exception handling in python is making code free of errors and exception which comes mostly from user input cometimes from ppogrammers end in big project, in this we use try and excpet block inside it we write the logic or risky code which can be faulty and gives error 



#Que 10:What is a module?
# modules in python are collection of predifiend methods which we can use in our code by importing them and using them to perform task operation and remove the unwanted time to wirte the code and logic which can we simply automated by the predifined methods 



#Section C: Code Understanding (5 marks each)
#Que 11: Find Output:
# Python
# x = [1,2,3]
# for i in x:
#     x.append(i)
#     if len(x) > 5:
#         break
# print(x)
# Ans: 1,2,3,1,2,3,4


# Que 12 Find error:
# Python
# def add(a, b):
#     print(a + b)

# result = add(2,3)
# print(result)
# Ans: error is there should be a return a+b instead of print(a+b) 


#  Total: 45 marks
# Scored : 29 marks 












# --------------------------------//-----------------------------------------//--------------------------------------------
# Logic Building (15 Days )
# Day 1 (29/03/2026)

# Ques 1: Print numbers from 1 to 10
# for i in range(1,11):
#     print(i)

# Ques 2: print even numbers from (1,20)
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)


# # Ques 3: Reverse String(loop)
# string = "1234"
# result = ""
# for i in range(len(string)-1,-1,-1):
#     string[i]
#     result = result + string[i]
# print(result)






# #Que 4: Remove duplicates from list
# l = [1,2,3,4,1,2,3,4]
# m = []
# for i in l:
#     if i not in m:
#      m.append(i)
# print(m)


#Que 5: find the second largest element in list 
# l = [1,2,5,2,1,3,4]
# m = l[0]
# for i in l:
#      if i > m:
#       m= i
# print(m)





# Smallest Element 
# l = [1,2,5,2,1,3,4]
# m = l[0]
# for i in l:
#      if i < m:
#       m= i
# print(m)


a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
if a > b:
    print("a is greater than b")
elif a < b:
    print("b is greater than a")
else:
    print("a and b are equal")



# Smallest Even number 
# l = [1,2,5,2,1,3,4]
# m = l[0]
# for i in l:
#      if i % 2 == 0 > m:
#       m= i
# print(m)



# l = [1,2,5,2,1,3,4]
# m = []
# for i in l:
#     if i % 2 ==0:
#         m.append(i)

# print(len(m))


