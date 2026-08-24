age=int(input("Enter your age: "))
if age<5:
    print("Ticket is free")
elif age>=5 and age<=17:
    print("Ticket price is 100rs")
elif age>=17 and age<=59:
    print("Ticket price is 200rs")
else:
    print("Ticket price is 120rs")