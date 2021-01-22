"""Find two largest values from 10 numbers input using nested control statement"""

max1 = int(input("Enter number #1: "))
max2 = int(input("Enter number #2: "))

if max1 < max2:
    max1, max2 = max2, max1

for i in range(3, 11):
    num = int(input(f"Enter number #{i}: "))
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

print(f"Largest number is: {max1}")
print(f"Second largest number is: {max2}")
