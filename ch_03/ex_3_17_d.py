"""Print out the following:
01)          *
02)         **
03)        ***
...
09)  *********
10) **********
"""

for i in range(10, 0, -1):
    for j in range(i - 1):
        print(" ", end="")
    for k in range(10 - i + 1):
        print("*", end="")
    print()

