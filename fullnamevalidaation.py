full_name = input("Enter your full name: ")
if ' ' in full_name and full_name[0]!=' ' and full_name[len(full_name)-1]!=' ':
    print("Full name is valid")
else:
    print("Full name is not valid")