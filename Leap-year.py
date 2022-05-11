Year = int(input("Enter the number: "))

if((Year % 400 == 0) or(Year % 100 != 0) and (Year % 4 == 0)):   
    print(str(Year) + " is a leap Year");
else:
    print (str(Year) +" is not a leap Year")  