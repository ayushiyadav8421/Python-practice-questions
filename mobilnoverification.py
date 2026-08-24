mobile_no = input("Enter mobile no: ")
if len(mobile_no)==10 and  mobile_no.isdigit():
    print("Mobile no is valid")
else:
    print("Mobile no is not valid")