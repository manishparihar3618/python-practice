x = int(input("Enter the value of x: "))
#x is variable to match , we can say this program will try to match with different cases .
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _:
        print(x)
        #default case will only be matched only if above cases are not matched
        