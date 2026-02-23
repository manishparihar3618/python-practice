
# #Question 2 *
# a = [1,2,3,4]
# b = [1,2,3,4]

# a1 = 23
# b1 = 23

# print(a is b)
# print(a == b)

# print(a1 == b1)
# print(a1 is b1)
# # == compares exact value 
# # is compares memeory location 


# # Question 3 **
# a = int(input("Enter a number: "))
# if a > 0:
#     print("Its a positive number ")
 
# elif a == 0:
#     print("Its Zero")

# else:
#     print("Its negative number ")
# # Use of if else elif : always use : After if else statments 


# # Question 4
# a = int(input("Enter a number: "))
# print("Positive") if a>0 else print("Zero") if a == 0 else print("Negative")

# # Question 5
# a = 6
# b = 2
# x = a+b
# x = a-b
# x = a*b
# x = a/b
# match x:
#     case 8:
#         print("Addition is :" ,x)
#     case 4:
#         print("Addition is :" ,x)
#     case 12:
#         print("Addition is :" ,x)
#     case 3:
#         print("Addition is :" ,x)

#     case _:
#         print("No match found") 






# for i in range(1,21):
#  if i%7 == 0 :
#    break
#  print(i)




# for i in range(1,21):
#  if i %2 == 0:
#     continue
#  print(i)



# # for i in range():


# for i in range(1,6):
#   print(i)
  
# else:
#     print("Sorry")



# num = int(input("Enter a number: "))
# if num>1:
#  for i in range(2,num):
#     if (num % i) == 0:
#         print(num, "is not a prime number")
#         break
#  else:
#     print(num, "is a prime number")     

  








# Program 11
str1 = str(input("Enter your String: "))
print(str1[0])
n=len(str1)
print(str1[n-1])
print(rev(str1))
