color = {"Red","Blue","Yellow" ,"Black","Grey"}
color2 = {"Pink"}
color.update(color2)
print(color)


color = {"Red","Blue","Yellow" ,"Black","Grey"}
color.discard("Blue")
print(color)


color = {"Red","Blue","Yellow" ,"Black","Grey"}
color2 = {"Pink","White","Purple"}
color.update(color2)
print(color)


color = {"Red","Blue","Yellow" ,"Black","Grey"}
color2 = {"Pink"}
color.pop()
print(color)


color = {"Red","Blue","Yellow" ,"Black","Grey"}
color2 = color.copy()
print(color2)

a = {1, 2, 3}
b = {3, 4, 5}
c =a.union(b)
print(c)










# its time for mediumlevel questions 
a = {1, 2, 3, 4}
b = {3, 4, 5}
c =a.intersection(b)
print(c)


a = {1, 2, 3}
b = {3, 4, 5}
c = {5, 6, 7}
a.update(b)
print(a)
a.update(c)
print(a)






a = {1, 2, 3}
b = {3, 4, 5}
c =a.symmetric_difference(b)
print(c)

