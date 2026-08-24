# m=int(input("Enter the size of list:"))
# num=[0]*m
# for i in range(m):
#     num[i]=int(input("Enter number:"))
# print(num)
# largest=num[0]
# for j in range(m):
#     if num[j]>largest:
#         temp=largest
#         largest=num[j]
#         num[j]=temp
# print(num)
# print(num[1])
m = int(input("Enter the size of list: "))
num = [0] * m
for i in range(m):
    num[i] = int(input("Enter number: "))
print(num)
for i in range(m):
    for j in range(0, m - i - 1):
        if num[j] > num[j + 1]:
            temp = num[j]
            num[j] = num[j + 1]
            num[j + 1] = temp

print(num)
print("Second largest:", num[m - 2])

