"""Calculate constant e by using the formula:
e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!"""

e = 1
denominator = 1

for i in range(1, 15):
    denominator *= i
    print(f"Denominator is: {denominator}")
    e += 1/denominator

print(e)
