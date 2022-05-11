hour = int(input("Enter the current hour: "))
minute = int(input("Enter the current minute: "))

if hour >= 0 and hour <=24 and minute >= 0 and minute <=60:
    futureTime = minute + 1;
    print("In one minute it will be: " + str(hour) +"h "+ str(futureTime) + "m");
else:
    print("Please enter a valid time");
