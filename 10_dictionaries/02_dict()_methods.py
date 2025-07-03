#Dictionary Methods:- dictionary uses several bulit-in methods for manipulation. They are listed below
#dictionary in python is ordered 
#--------update()-------
ep1 = {122: 45, 123: 89, 567 :69, 670 :69}
ep2 ={222: 67, 566: 90}

ep1.update(ep2)
print(ep1) #ep1 will update itself 

# -------clear()---------
ep1.clear()
print(ep1)#will print empty dictionary {}

#--------pop()-----------
ep1 = {122: 45, 123: 89, 567 :69, 670 :69}
ep2 ={222: 67, 566: 90}
ep1.pop(122)
print(ep1)#remove 122: 45

#--------popitem()---------
ep1.popitem()#remove last last key value pair from dictionary.

#----------del------------
# del ep1
# print(ep1)
del ep1[123]
print(ep1)