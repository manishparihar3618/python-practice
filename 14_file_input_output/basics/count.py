f = open('myfile2.txt', 'r')
count = 0
for line in f:
    count += 1   # increase by 1 for every line

print("Total number of lines:", count)
f.close()