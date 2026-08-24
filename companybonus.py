salary=float(input("Enter your salary: "))
years=int(input("Enter number of years in service: "))
if years>=10:
    bonus=salary*20/100
    print("Your bonus is Rs",bonus)
    print("Salary including bonuses", salary+bonus)
elif years>=5:
    bonus=salary*10/100
    print("Your bonus is Rs",bonus)
    print("Salary including bonuses", salary+bonus)
elif years>=2:
    bonus=salary*5/100
    print("Your bonus is Rs",bonus)
    print("Salary including bonuses", salary+bonus)
else:
    print("No bonuses")
    print("Salary including bonuses", salary)