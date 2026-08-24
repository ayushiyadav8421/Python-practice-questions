marks=int(input("Enter your marks:"))
if marks>=40:
    print("Pass")
elif marks>=35 and marks<=39:
    marks+=5
    print("Pass")
else:
    print("Fail")