# Exercise 09_05 from Deitel: Intro to Python and CS

"""
Modify your solution to the preceding exercise
Create a grade report that displays each student’s average to the right of that student’s row and
the class average for each exam below that exam’s column.

Previous exercise 9.4:
Use the csv module to read the grades.csv file from the previous exercise. Display the data in tabular format.

Previous exercise 9.3:
Use the csv module to write each record into the grades.csv file.
Each record should be a single line of text in the following CSV format:
firstname,lastname,exam1grade,exam2grade,exam3grade
"""

import csv

# Initialize counter for students and totals for each exam
counter_students = 0
total_exam_1 = 0
total_exam_2 = 0
total_exam_3 = 0

# Open file written with writelines
with open("ex_09_03_grades_std.csv", mode='r', newline='') as grades:
    reader = csv.reader(grades)
    print(f"{'First name':<14}{'Last name':<14}{'Exam 1':>8}{'Exam 2':>8}{'Exam 3':>8}{'Ind.Avg.':>10}")
    for record in reader:
        # Increase counter of students by 1
        counter_students += 1
        first, last, exam1, exam2, exam3 = record    # unpack record
        stud_average = (float(exam1) + float(exam2) + float(exam3)) / 3    # calculate student's average
        print(f"{first:<14}{last:<14}{exam1:>8}{exam2:>8}{exam3:>8}{stud_average:>10.2f}")
        # Update exam totals
        total_exam_3 += float(exam3)
        total_exam_2 += float(exam2)
        total_exam_1 += float(exam1)

print(f"{'AVERAGE GRADES PER EXAM:':>28}{total_exam_1 / counter_students:>8.2f}"
      f"{total_exam_2 / counter_students:>8.2f}{total_exam_3 / counter_students:>8.2f}")

