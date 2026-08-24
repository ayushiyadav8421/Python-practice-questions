m=int(input("Enter the number of students: "))
marks=[0]*m
for i in range(m):
    marks[i]=int(input("Enter marks: "))
print (marks)
pos= int(input("Enter the position of the student: "))
num= int(input("Enter the numer to add:"))
updated_marks=[0]*(m+1)
for j in range(len(updated_marks)):
    if j<pos:
        updated_marks[j]=marks[j]
    elif j==pos:
        updated_marks[j]=num
    else:
        updated_marks[j]=marks[j-1]
print (updated_marks)
# m= int(input("enter size of list:"))
# nums=[0]*m
# for i in range(m):

