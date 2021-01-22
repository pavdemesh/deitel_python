"""Combine all 4 patterns a through d from exercise 3_17"""

for row in range(1, 11):
    # Draw 1st pattern
    for j in range(row):
        print("*", end="")
    for k in range(10 - row):
        print(" ", end="")
    print("   ", end="")

    # Draw 2nd pattern
    for m in range(10 - row + 1):
        print("*", end="")
    for n in range(row - 1):
        print(" ", end="")
    print("   ", end="")

    # Draw 3rd pattern
    sign = "*" * (10 - row + 1)
    print(f"{sign:>10}", end="")
    print("   ", end="")

    # Draw 4th pattern
    sign = "*" * row
    print(f"{sign:>10}", end="")
    print()
