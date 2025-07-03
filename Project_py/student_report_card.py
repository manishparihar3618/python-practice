students = [
    ["Alice",   92, 88, 85, 94, 78],
    ["Bob",     65, 70, 58, 60, 50],
    ["Charlie", 35, 40, 30, 20, 45],
    ["David",   89, 84, 91, 95, 93],
    ["Eve",     76, 79, 68, 72, 80],
    ["Frank",   58, 62, 60, 55, 70],
    ["Grace",   90, 91, 89, 92, 88],
    ["Hannah",  47, 55, 50, 48, 53],
    ["Ivan",    69, 73, 77, 65, 71],
    ["Judy",    88, 85, 90, 87, 86],
    ["Kevin",   42, 40, 39, 45, 43],
    ["Laura",   95, 92, 93, 96, 94],
    ["Mike",    80, 75, 78, 82, 79],
    ["Nina",    55, 60, 50, 57, 59],
    ["Oscar",   61, 64, 68, 66, 63]
]
print("------ STUDENT MARKS REPORT ------\n")

for student in students:
    name = student[0]
    marks = student[1:]
    total = sum(marks)
    average = total / len(marks)

    print(f"Name       : {name}")
    print(f"Total      : {total} / 500")
    print(f"Average    : {average:.2f}%")

    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 40:
        grade = 'D'
    else:
        grade = 'F'

    print(f"Grade      : {grade}")
    print("----------------------------------\n")
