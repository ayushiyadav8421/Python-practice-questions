speed= int(input("Enter your speed : "))
if speed<=60:
    print("No fine")
elif speed>60 and speed<=80:
    print("Fine of Rs 500")
elif speed>80 and speed<=100:
    print("Fine of Rs 1000")
else:
    print("Fine of Rs 2000+ license warning")