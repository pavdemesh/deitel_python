"""Print out the following:
01) **********
02) *********
03) ********
...
10) *
"""

for i in range(10, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
