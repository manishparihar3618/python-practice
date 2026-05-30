
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

  








# <<<<<<< HEAD
# # Program 11
# str1 = str(input("Enter your String: "))
# print(str1[0])
# n=len(str1)
# print(str1[n-1])
# print(rev(str1))
# =======
# # Program 11
# str1 = str(input("Enter your String: "))
# print(str1[0])
# n=len(str1)
# print(str1[n-1])
# print(rev(str1))















# Question 1 (input)
# name = input("Enter your name: ")
# age = int(input("Age: "))
# print(name)
# print(age)

# Question 2 (Swapping)
# with third variable
# a = 12
# b = 32
# temp = a
# a = b
# b = temp
# print(a)
# print(b)
# # without 3rd variable
# a,b = b,a 
# print(a)
# print(b)


#Question 3
# celsius = float(input("Enter temparature in celsius: "))
# fahrenheit = (celsius*1.8)+32
# print(fahrenheit)



# #Question 4 (Average)
# a = 34 
# b = 22
# c = 19
# avg = (a+b+c)/3
# print(avg)


# # Question 5 (ASCII)
# asci= str(input("Enter caharacter: "))
# asciii=ord(asci)
# print(asciii)



# Question 6 (Minutes into hours)
# min = int(input("Enter minutes: "))
# if (min < 60):
#     print(min," minutes")
# elif(min == 60):
#     print("1 hour")
# else :
#     hours = min//60 
#     print(hours,"Hours")
#     minutes = min % 60
#     print(minutes,"min")
    


# # Question 7(Find square and cube) 
# a = int(input("Enter the number: "))
# sqr = a*a
# cube = a*a*a
# print(f"Square will be: {sqr} and Cube will be: {cube}")



# Question 8(cheak input type)
# a = int(input("Enter: "))
# b = float(input("Enter : "))
# print(type(b))
# print(type(a))
# print(a)





### SECTION 2

# Question 9(Number is negative positive or zero)
# number = int(input("Enter the number: "))
# if(number> 0):
#     print("Positive Number")
# elif(number == 0):
#     print("Zero")
# else:
#     print("Negative Number ")


#Question 10(Find largest of 3)
# num1 = 75000
# num2 = 5500
# num3 = 744
# if (num1 > num2 and num1 >num3):
#      print("num1 is largest")

# elif(num2 > num1 and num2>num3):
#      print("num2 is largest")

# else:
#      print("num3 is largest")







#Question 11(leap year)
# year = int(input("Enter year: "))
# if (year%4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("leap year")

# else: 
#     print("not a leap year")



#Question 12(Grade System)
# marks = 65
# if ( marks <= 33):
#     print("Fail")
# elif(33 <= marks and marks <= 50):
#     print("C grade")
# elif(51 <= marks and marks <= 70):
#     print("B Grade")
# elif(71 <= marks and marks <= 90):
#     print("A Garde")
# else:
#     print("O Grade")



#Question 13(Cheak if character is vowel or consonent)
# character = input("Enter character: ")
# if (character == "a" or  character =="e" or character == "i" or character =="o" or character =="u"):
#     print("Its A Vowel")
# else :
#     print("Its a Consonent")



#Question 14 (Simple clac)
# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# c = input("Enter Operation: ")
# if ( c == "+"):
#     print("Addition is: ",a+b)
# elif( c == "-"):
#     print("Substraction is: ",a-b)
# elif(c == "*"):
#     print("Multiplication is: ",a*b)
# elif(c == "/"):
#     print("Division is: ",a/b)
# else:
#     print("Enter a valid operator")




# #Question 15(number is divisilbe by 5 and 11)
# a = int(input("Enter the number: "))
# if ((a % 5 == 0) and (a % 11 == 0)):
#     print("Divisilbe by 5 and 11")
# else:
#     print("Not Divisible by 5 and 11")





#Section 3(Loops)

#Question 16(Print 1 to N)
# N = int(input("Enter range: "))
# for i in range(1,N+1):
#     print(i)



#Question 17 (Sum of first N numbers )
# sum = 0
# N = int(input("Enter range: "))
# for i in range(1,N+1):
#     sum = sum + i
# print(sum)
  


#Question 18(Factorial using loop)
# factorail = 1
# for i in range(1,5):
#     factorail = factorail * i
# print(factorail)




#Question 19(Reverse a number)
# a = "3456"
# for i in range(len(a)-1,-1,-1):
#     print(a[i])




#Question 20(count digits)
# count = 0
# a = "122334"
# for i in a:
#     count = count +1
# print(count)




# #Question 21(fibbonaci series)
# n = int(input("Enter number: "))
# a = 0
# b = 1
# for i in range(n):
#    print(a)
#    c = a+b
#    a = b
#    b = c




## Question 22
# n = int(input("Enter numbers: "))
# for i in range(2,n+1):
#     is_prime = True
#     for j in range(2,i):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i)


#Question 23 (loop of traingle pattern)
# loop = 5
# for i in range(1,8):
#     print(" *"*i)



#Question 24 (Multiplication Table)
# a = int(input("Print Multiplication table of: "))
# for i in range(1,11):
#     print(f'{a} * {i} =  ',a*i)


# #Question 25 (Sum of Digits)
# a = "123"
# sum = 0
# for i in a:
#     sum = sum + int(i)

# print(sum)




### Section - 4 (Strings)
#Question 26(Reverse a string)

# a = input("Enter Any String: ")
# for i in range(len(a)-1,-1,-1):
#     print(a[i])



## Question 27 (Cheak palindrome)
# a = int(input("Enter a number: "))
# rev = ""
# for i in range(len(str(a))-1,-1,-1):
#     rev = rev + str(a)[i]
    
# if a == int(rev):
#         print("Its a palindrome")
# else:
#     print("Its not a palindrome")



##Question 28 (Count Vowels and Consonents)
# b = ""
# a = input("Enter a string: ")
# for i in a:
#     b = a.count(a)
# print(b)



# 
# string  = "Python is a scripting language"
# print("a appeared: ",string.count("a"),"times")





#Question 29 (Remove duplicates from string)










# -------------------------------//-----------------------------------------
# Q1. Write a function that takes a number and returns its square
# def squareof (a):
#     return a * a
    
# print(squareof(14))



# Q2. Write a function is_even(n) that returns True if number is even else False
# def even(b):
#     if b % 2 == 0 :
#         return True 
#     else :
#         return False
# print(even(7))



# Q3. Write a function that takes a list and returns sum of elements
# def sum1(lst):
#     total = 0
#     for num in lst:
#      total = total + num

#     return total

# print(sum1([1,2,3,4]))




#Q4. Find largest element in a list (without using max())
# def largest1(lst):
#     largest = lst[0]
#     for i in lst:
#      if largest < i:
#         largest = i
#     return(largest)

# print(largest1([1,2,3,31,2,4,52]))




#Q5 Q5. Remove duplicates from list
# Input: [1,2,2,3,4,4]
# Output: [1,2,3,4]






## Q1. Reverse a string using recursion
# Input: "hello"
# Output: "olleh"

def reversal(a):
    for i in range(len(a)-1,-1,-1):
        return (a[i])


reversal("hello")

# a = "3456"
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

