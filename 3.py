marks = input("Enter marks: ").split()

b = int(input("Enter index to update the marks: "))
c = int(input("Enter marks to update: "))

marks[b] = str(c)

print(marks)
