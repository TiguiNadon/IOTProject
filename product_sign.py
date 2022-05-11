int1 = float(input("Enter number 1: "))
int2 = float(input("Enter number 2: "))

if int1 > 0 and int2 > 0:
    print("The product is positive")
elif int1 < 0 and int2 > 0:
    print("The product is negative")
elif int1 > 0 and int2 < 0:
    print("The product is negative")
elif int1 < 0 and int2 < 0:
    print("The product is positive")