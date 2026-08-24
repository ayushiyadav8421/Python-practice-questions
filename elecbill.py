unit= float(input("Enter your unit: "))
if unit>=0 and unit<100:
    bill= unit*1.5
    print("Your bill is ",bill,"rs")
    print("Electricity bill including service charges:",bill+50)
elif unit>=100 and unit<200:
    bill= unit*2.5
    print("Your bill is ",bill,"rs")
    print("Electricity bill including service charges:", bill + 50)
elif unit >= 200 and unit <= 300:
    bill= unit*3.5
    print("Your bill is ",bill,"Rs")
    print("Electricity bill including service charges:", bill + 50)
else:
    bill=unit*6
    print("Your bill is ",bill,"rs")