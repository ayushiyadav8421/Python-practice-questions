nums=input("Enter 2 numbers separated by space: ").split()
n=len(nums)
d=[]
for i in range(n):
    if nums[i].isdigit():
        print("value accepted")
        d.append(int(nums[i]))
    else:
        print("ValueError")
        print("IndexError")

def division(d):
    a=d[0]
    b=d[1]
    if a==0:
        print("DivisionError")
    else:
        div=b/a
        return div
res=division(d)

