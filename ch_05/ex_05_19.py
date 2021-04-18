"""
Create a list of tuples containing first and last names.
Use filter() to locate the tuples containing the last name Jones.
Ensure that several tuples in your list have that last name.
"""

names = [("Amanda", "Jones"), ("MIke", "Petersen"), ("Frank", "Jones"), ("Sandy", "Holger")]

list_of_jones_1 = list(filter(lambda x: x[1] == "Jones", names))

print(list_of_jones_1)
