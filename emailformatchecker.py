email_id=input("Enter your email: ")
if '@' in email_id and '.' in email_id and email_id[0]!='@':
    print("Email is valid")
else:
    print("Email is not valid")