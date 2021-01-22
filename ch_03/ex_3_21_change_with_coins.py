"""Given quarters (25 cent), dimes (10 cent), nickels (5 cent) and pennies (1 cent):
Calculate how to give change with fewest coins possible"""

change_in_cents = int(input("Enter the amount of required change in cents: "))

quarters = 0
dimes = 0
nickels = 0
pennies = 0

while change_in_cents > 0:
    if change_in_cents >= 25:
        change_in_cents -= 25
        quarters += 1
    elif change_in_cents >= 10:
        change_in_cents -= 10
        dimes += 1
    elif change_in_cents >= 5:
        change_in_cents -= 5
        nickels += 1
    elif change_in_cents > 0:
        change_in_cents -= 1
        pennies += 1

print(f"quarters:\t{quarters:>2}")
print(f"dimes:\t\t{dimes:>2}")
print(f"nickels:\t{nickels:>2}")
print(f"pennies:\t{pennies:>2}")
