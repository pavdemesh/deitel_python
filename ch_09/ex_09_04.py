# Exercise 09_04 from Deitel: Intro to Python and CS

"""
Use the csv module to read the grades.csv file from the previous exercise. Display the data in tabular format.
Previous exercise 9.3:
Use the csv module to write each record into the grades.csv file.
Each record should be a single line of text in the following CSV format:
firstname,lastname,exam1grade,exam2grade,exam3grade
"""

import csv

# Open file written with writelines
with open("ex_09_03_grades_std.csv", mode='r', newline='') as grades:
    reader = csv.reader(grades)
    print(f"{'First name':<14}{'Last name':<14}{'Exam 1':>8}{'Exam 2':>8}{'Exam 3':>8}")
    for record in reader:
        first, last, exam1, exam2, exam3 = record
        print(f"{first:<14}{last:<14}{exam1:>8}{exam2:>8}{exam3:>8}")

print()

# Open file written with csv module and writerow
with open("ex_09_03_grades_csv.csv", mode='r', newline='') as grads:
    reader = csv.reader(grads)
    students = list(reader)
    print(*students)
