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
        





# Example
day = int(input("Enter day number (1–7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")




# Multiple match
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid input")
