amount=float(input("Enter your amount: "))
withdraw=float(input("Enter your withdrawal amount: "))
if withdraw%100==0 and withdraw<=amount:
    amount = amount-withdraw
    if amount>=500:
        print("You can withdraw the required amount")
    else:
        print("You cannot withdraw the required amount")
else:
    print("You cannot withdraw the required amount")