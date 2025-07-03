# # try:
# #     a = int(input("Enter 1st number:- "))
# #     b = int(input("Enter 2st number:- "))
# #     print(f"{a} + {b} is:-",a + b)
# #     print(f"{a} - {b} is:-",a - b)
# #     print(f"{a} x {b} is:-",a * b)
# #     print(f"{a} / {b} is:-",a / b)
# # except ValueError:
# #     print("Please Enter Integer value")
# # except ZeroDivisionError:
# #     print("Dividing any number with zero is not possible")



# # try:
#     # a = int(input("Enter 1st number:- "))
#     # b = int(input("Enter 2st number:- "))

#     # print(f"{a} + {b} is:-",a + b)
#     # print(f"{a} - {b} is:-",a - b)
#     # print(f"{a} x {b} is:-",a * b)
# #     print(f"{a} / {b} is:-",a / b)
# # # except ValueError:
# # #     print("Please Enter Integer value")
# # # except ZeroDivisionError:
# # #     print("Dividing any number with zero is not possible")






# # try:
# #  a = int(input("Enter a number: "))
# #  print("Square is",a * a)
# # except ValueError:
# #  print("Enter valid integer")


# try:
#  list = [2,3,3,5,6]
#  a = int(input("Enter Index of number you want to access: "))
#  b = list[a]
#  print(f"Value at index {a} is  ",b)
# except ValueError:
#  print("Value error")
# except IndexError:
#  print("Index error")

try:
  a = input("Enter your password:- ")
  if len(a)<6:
      raise ValueError("Password is very small")
except ValueError:
 print("Invalid input")
















