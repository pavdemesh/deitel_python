"""Print out the following:
01) **********
02)  *********
03)   ********
...
09)         **
10)          *
"""

for i in range(10):
    for j in range(i):
        print(" ", end="")
    for k in range(10 - i):
        print("*", end="")
    print()

