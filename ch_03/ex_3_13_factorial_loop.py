"""Calculate factorial using for loop"""


def fn_factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


print(fn_factorial(5))
print(fn_factorial(6))
print(fn_factorial(4))
