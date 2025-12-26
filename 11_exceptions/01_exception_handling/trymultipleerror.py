try:
    num = int(input("Enter an integer: "))
    a = [6,3]
    print(a[num])#indexing
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")
    