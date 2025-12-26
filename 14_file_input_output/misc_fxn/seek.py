with open('file.txt','r') as f:
    f.seek(10)#Move to 10th byte in file 
    data = f.read(14)#Read next 14 bytes
    print(data)