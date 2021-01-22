"""Print out the following:
01) **********
02)  *********
03)   ********
...
09)         **
10)          *
"""

# This solution uses right alignment in a field of width 10
for i in range(10, 0, -1):
    sign = "*" * i
    print(f"{sign:>10}", end="")
    print()
