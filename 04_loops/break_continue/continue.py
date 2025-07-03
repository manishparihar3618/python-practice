for i in range(12):
    if(i==10):
      continue
    print(i)
#continue statment means it will skip the condition to  print and after skipping that iteration it will again start printing next values .In above programm it will be skipping 10  because we gave condition to that iteration that when i=10 comes skip it and start printing again
# we can also modify the programmm by printing
for i in range(12):
    if(i==10):
      print("skip the iteration")
      continue
    print(i)#this program will be print skip the iteration where we have to skip the condition




















a = "34"
for i in a:
  if(i==6):
    continue
    print(i)
    i = i-1