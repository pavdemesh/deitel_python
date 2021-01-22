"""Read a 5-digit number and determine if it is a palindrome.
Use // and % operators to separate the number into its digits."""

number = int(input("Enter a 5-digit number: "))

first_digit = number // 10_000
last_digit = number % 10

if first_digit == last_digit:
    second_digit = number // 1_000 % 10
    fourth_digit = number % 100 // 10
    if second_digit == fourth_digit:
        print("Is palindrome")
    else:
        print("Not palindrome")
else:
    print("Not palindrome")
