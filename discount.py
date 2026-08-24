amount= int(input("enter the amount:"))
if amount>=2000:
    price= amount-(amount*20)/100
    print("Final price of the product is",price)
elif amount>=1000 :
    price= amount-(amount*10)/100
    print("Discount on the product is",price)
elif amount>=500 :
    price= amount-(amount*5)/100
    print("Discount on the product is",price)
else:
    print("There is no discount on the product, so the price is",amount)