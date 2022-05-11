grade = int(input("Your grade: "))
totalPoint = int(input("Out of: "))

def mathFunction(points, totalpoints):
    grade = points / totalpoints * 100
    if grade > 80:
        print("Your grade is a")
    elif grade > 60 and grade < 80:
        print("Your grade is b")
    elif grade > 50 and grade < 60:
        print("Your grade is c")
    elif grade > 40 and grade < 60:
        print("Your grade is d")
    elif grade < 40:
        print("Your grade is e");

mathFunction(grade, totalPoint)
