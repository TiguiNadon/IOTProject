salary = float(input("Salary per hour: "))
hours = float(input("Hours worked: "))

def mathFunction(salary, hours):
    if hours <= 39:
        pay = salary * hours;
        print("You have made: " + str(pay) + " dollars")
        print("Overtime hours worked: 0");
    elif hours >= 40 and hours <= 44:
        overtimeHours = hours - 39;
        pay = salary * hours;
        overtimePay = salary * 1.5 * overtimeHours;
        overtimeSalary = salary * 1.5;
        totalPay = overtimePay + pay;
        print("Normal pay: " + str(pay) + " dollars");
        print("You have made: " + str(totalPay) + (" dollars"));
        print("Overtime hours worked: " + str(overtimeHours));
        print("Overtime salary: " + str(overtimeSalary) + " dollars per hour");
        print("Money made in overtime: " + str(overtimePay) + " dollars");
    elif hours >= 45 and hours <= 49:
        overtimeHours = hours - 39;
        pay = salary * hours;
        overtimePay = salary * 1.75 * overtimeHours;
        overtimeSalary = salary * 1.75;
        totalPay = overtimePay + pay;
        print("Normal pay: " + str(pay) + " dollars");
        print("You have made: " + str(totalPay) + (" dollars"));
        print("Overtime hours worked: " + str(overtimeHours));
        print("Overtime salary: " + str(overtimeSalary) + " dollars per hour");
        print("Money made in overtime: " + str(overtimePay) + " dollars");
    elif hours >= 50:
        overtimeHours = hours - 39;
        pay = salary * hours;
        overtimePay = salary * 2 * overtimeHours;
        overtimeSalary = salary * 2;
        totalPay = overtimePay + pay;
        print("Normal pay: " + str(pay) + " dollars");
        print("You have made: " + str(totalPay) + (" dollars"));
        print("Overtime hours worked: " + str(overtimeHours));
        print("Overtime salary: " + str(overtimeSalary) + " dollars per hour");
        print("Money made in overtime: " + str(overtimePay) + " dollars");
        
mathFunction(salary, hours)