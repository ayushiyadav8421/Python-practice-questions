num=int(input("Enter seat number: "))
if num>=1 and num<=5:
    print("Ticket price is Rs 250")
elif num>5 and num<=10:
    print("Ticket price is Rs 200")
elif num>10 and num<=15:
    print("Ticket price is Rs 100")
else:
    print("Invalid seat number")