user_n=input("Enter your username: ")
user_p=input("Enter your password: ")
if user_n and len(user_p)>=8:
    print("Login successful")
else:
    print("Login failed")