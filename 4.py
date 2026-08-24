nums = input("Enter 2 numbers separated by space: ").split()
d = []
for i in range(len(nums)):
    try:
        val = int(nums[i])
        print("Value accepted")
        d.append(val)
    except ValueError:
        print("ValueError")
if len(d) < 2:
    print("IndexError")
else:
    def division(d):
        a = d[0]
        b = d[1]

        if b == 0:
            print("DivisionError")
        else:
            return a / b
    res = division(d)
    if res is not None:
        print("Result:", res)