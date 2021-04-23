"""In each of the following expressions, replace the ***s with a set operator
that produces the result shown in the comment. 
The last operation should check whether the left operand is an improper subset of the right operand. 
For each of the first four expressions, specify the name of the set operation 
that produces the specified result.
"""

# a) {1, 2, 4, 8, 16} *** {1, 4, 16, 64, 256} ====> {1, 2, 4, 8, 16, 64, 256}
if ({1, 2, 4, 8, 16} | {1, 4, 16, 64, 256}) == {1, 2, 4, 8, 16, 64, 256}:
    print("Task a) successful. Set operator: union (|). Returns uniqe elements from both sets.")

# b) {1, 2, 4, 8, 16} *** {1, 4, 16, 64, 256} ====> {1, 4, 16}
if {1, 2, 4, 8, 16} & {1, 4, 16, 64, 256} == {1, 4, 16}:
    print("Task b) successful. Set operator: intersection (&). Returns common elements in both sets")

# c) {1, 2, 4, 8, 16} *** {1, 4, 16, 64, 256} ====> {2, 8}
if ({1, 2, 4, 8, 16} - {1, 4, 16, 64, 256}) == {2,8}:
    print("Task c) successful. Set operator: difference (-). Returns uniqe elements from left operand.")

# d) {1, 2, 4, 8, 16} *** {1, 4, 16, 64, 256} ====> {2,8,64,256}
if ({1, 2, 4, 8, 16} ^ {1, 4, 16, 64, 256}) == {2, 8, 64, 256}:
    print("Task d) successful. Set operator: symmetric difference (^). Returns uniqe from left operand and right operand.")

# e) {1, 2, 4, 8, 16} *** {1, 4, 16, 64, 256}  ====> False
if ({1, 2, 4, 8, 16} <= {1, 4, 16, 64, 256}) == False:
    print("Task e) successful. Set operator: is improper subset (<). Returns True or False.")
