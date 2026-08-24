import math
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def prime(n):
    for num in nums:
        if num<=1:
            return 0;
        if num%(sqrt(num))!=0:
            return num
def divide(nums):
    for num in nums:
        if num%5==0:
            return num
nums=fibonacci(10)
print(prime(nums))
print(divide(nums))
