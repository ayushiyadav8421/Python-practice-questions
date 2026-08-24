level=float(input("Enter level of water in the tank(in percentage): "))
if level>=0 and level<=20:
    print("Water level in tank is low")
elif level>20 and level<=70:
    print("Water level in tank is normal")
elif level>70 and level<=100:
    print("Water level in tank is high")
else:
    print("Entered level is invalid")
