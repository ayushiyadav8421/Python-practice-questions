import math
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def divisible_by_5(n):
    return n % 5 == 0
num = fibonacci(10)
print("Fibonacci:", num)
print("Is prime?:", is_prime(num))
print("Divisible by 5:", divisible_by_5(num))