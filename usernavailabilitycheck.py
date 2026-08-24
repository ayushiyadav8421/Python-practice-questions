user_n=input("Enter your username: ")
if '' in user_n and len(user_n)<5:
    print("Username is not available")
else:
    print("username is available")