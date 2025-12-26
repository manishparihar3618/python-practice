# marks = [12,56,32,98,12,45,3,1,4]
# index = 0
# for marks in marks:
#     print(marks)
#     if(index == 3):
#         print("Harry, awesome")
#     index +=1




marks = [12,56,32,98,12,45,3,1,4]
for index, marks in enumerate (marks):
     print(marks)
     if(index == 3):
         print("Harry, awesome")



marks = [12,56,32,98,12,45,3,1,4]
for index, marks in enumerate (marks,start=1):
     print(marks)
     if(index == 3):
         print("Harry, awesome")