# d = {"Apple": "Fruit", 1: "One"}
# print(d["Apple"])
# print(d.values())


# dict1 = {344: "Manish", 234:"Harry"}
# dict1[344]

# marks = {101: 45, 102: 78, 103: 50, 104: 91}
# for keys in marks.keys():
#     if(marks[keys]>60):
#      print(marks[keys])


# data = {"a": 1, "b": 2}
# print(data.get("c"))



# ep = {122: 45, 123: 89, 567: 69, 670: 69}
# print(ep.pop(567))


info = {'name': 'Karan', 'age': '19', 'eligible': True}
info2 = {'gender':'Male'}
info.update(info2)
print(info)



scores = {101: 45, 102: 78, 103: 50, 104: 91}
count = 0
for value in scores.values():
    if value>50:
     count += 1
print(count)
