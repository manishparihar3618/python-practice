with open('file.txt','r') as f:
    f.seek(10)
    print(f.tell())#gives index at which we are
    data = f.read(14)
    print(data)