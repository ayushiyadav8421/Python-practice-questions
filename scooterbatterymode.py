battery = int(input("Enter battery percentage: "))
if battery > 70:
    print("Performance mode")
elif battery>=30 and battery<=70:
    print("Normal mode")
elif battery<30:
    print("Power Saving mode")
else:
    print("Invalid input")