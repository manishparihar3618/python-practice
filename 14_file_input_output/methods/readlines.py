f = open('myfile.txt','r')
while True:
    line = f.readline()
    print(line)
    if not line:
        # print(line,type(line))  #output class 'str
        break



f = open('myfile2.txt','r')
while True:
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student 1 in Maths is :{m1*2}")
    print(f"Marks of student 2 in Chemistry is :{m2*2}")
    print(f"Marks of student 3 in Physics is :{m3*2}")
    # print(line)
     