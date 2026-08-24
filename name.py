n= int(input("Enter the size of the list:"))
marks=[0]*n
for i in range(n):
    marks[i]=int(input("Enter the marks:"))
print(marks)
for i in range(n):
    print(marks[i])
    if marks[i]>=40:
        print("Pass")
    else:
        print("Fail")
delete= int(input("Enter the marks you want to delete:"))
for i in range(n):
    if marks[i]==delete:
        marks.remove(delete)
    else:
        print("Invalid marks")
print(marks)