age = input("Enter your age: ")
age1 = int(age)
if(age1 < 18):
  if(age1 >= 15):
    print("Okay we will be giving you 20ml dose")
  elif(10 <age1< 15):
    print("Okay we will be giving you 15ml dose")
  elif(5 <=age1<= 10):
    print("Okay we will be giving you 10ml dose")
  else:
    print("Sorry not eligible for vaccination")
elif(18 <=age1<= 65):
  print("")
  if(18 <=age1<= 55):
    print("Okay we will be giving you 25ml dose")
  else:
    print("Okay we will be giving you 20ml dose")
else:
  print("Not eligible for vaccination")