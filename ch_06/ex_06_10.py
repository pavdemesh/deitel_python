"""
Using the following sets:
{'red', 'green', 'blue'}
{'cyan', 'green', 'blue', 'magenta', 'red'}
display the results of:
a) comparing the sets using the each of the comparison operators.
b) combining the sets using each of the mathematical set operators.
"""

set_1 = {'red', 'green', 'blue'}
set_2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

print("--------------------------")

# Task a)
print("Task a): Compare the sets using the each of the comparison operators.")
print(f"{'set_1 is proper subset of set_2:':<40} {set_1 < set_2}")
print(f"{'set_1 is improper subset of set_2:':<40} {set_1.issubset(set_2)}")
print(f"{'set_1 is proper superset of set_2:':<40} {set_1 > set_2}")
print(f"{'set_1 is improper superset of set_2:':<40} {set_1.issuperset(set_2)}")

print("--------------------------")

# Task b)
print("Task b): Combine the sets using each of the mathematical set operators.")
print(f"{'Union:':<40} {set_1 | set_2}")
print(f"{'Intersection:':<40} {set_1 & set_2}")
print(f"{'Difference:':<40} {set_1 - set_2}")
print(f"{'Symmetric Difference:':<40} {set_1 ^ set_2}")
print(f"{'Isdisjoint:':<40} {set_1.isdisjoint(set_2)}")


