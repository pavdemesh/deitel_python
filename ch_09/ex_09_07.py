# Exercise 09_07 from Deitel: Intro to Python and CS

"""
Reimplement Exercise 9.4 using the json module to read the grades.json file created in the previous exercise.
Display the data in tabular format,
including an additional column showing each student’s average to the right of that student’s three exam grades and
an additional row showing the class average on each exam below that exam’s column.
"""

import json

# Initialize counter for students and totals for each exam
counter_students = 0
total_exam_1 = 0
total_exam_2 = 0
total_exam_3 = 0

# Open json file and load its contents into a dictionary
with open("ex_09_06_grades.json", mode='r') as fh_grades:
    grades_dict = json.load(fh_grades)

# Print header
print(f"{'First name':<14}{'Last name':<14}{'Exam 1':>8}{'Exam 2':>8}{'Exam 3':>8}{'Ind.Avg.':>10}")

# Iterate over the list of dictionaries (individual student's records)
for student in grades_dict['students']:
    # Increase counter of students by 1
    counter_students += 1

    # Extract data for each student from corresponding dictionary
    first = student["first_name"]
    last = student['last_name']
    exam1 = float(student['exam1'])
    exam2 = float(student['exam2'])
    exam3 = float(student['exam3'])

    # Calculate student's average
    stud_average = (exam1 + exam2 + exam3) / 3

    # Print formatted individual student's data
    print(f"{first:<14}{last:<14}{exam1:>8}{exam2:>8}{exam3:>8}{stud_average:>10.2f}")

    # Update exam totals
    total_exam_3 += exam3
    total_exam_2 += exam2
    total_exam_1 += exam1

# Print additional line of average for each exam
print(f"{'AVERAGE GRADES PER EXAM:':>28}{total_exam_1 / counter_students:>8.2f}"
      f"{total_exam_2 / counter_students:>8.2f}{total_exam_3 / counter_students:>8.2f}")
