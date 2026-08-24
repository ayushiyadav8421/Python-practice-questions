data_usage=int(input("Enter the data used in MB: "))
if data_usage<1500:
    print("safe")
elif data_usage>=1500 and data_usage<=2048:
    print("Warning")
else:
    print("extra charge of Rs 50")