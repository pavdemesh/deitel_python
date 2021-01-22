"""Print out the following:
01) *
02) **
03) ***
...
10) **********
"""

for i in range(1, 11):
    for j in range(i):
        print("*", end="")
    print()
