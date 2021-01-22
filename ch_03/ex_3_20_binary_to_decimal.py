"""Convert binary to decimal using modulo and division operators"""

binary = int(input("Enter binary representation of a number: "))

decimal = 0
last_digit = 0
multiplier = 1

while binary > 0:
    # Calculate last digit. Multiply digit by current multiplier and add to running decimal
    last_digit = binary % 10
    decimal = decimal + last_digit * multiplier
    # Update multiplier and get rid of currently last digit in binary representation
    multiplier *= 2
    binary //= 10

print(decimal)
