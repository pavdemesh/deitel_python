# Exercise 09_03 from Deitel: Intro to Python and CS

"""
An instructor teaches a class in which each student takes three exams.
The instructor would like to store this information in a file named grades.csv for later use.
Write code that enables an instructor to enter:
each student’s first name and last name as strings and the student’s three exam grades as integers.
Use the csv module to write each record into the grades.csv file.
Each record should be a single line of text in the following CSV format:
firstname,lastname,exam1grade,exam2grade,exam3grade
"""

import csv

# list of lists to store students data
students = list()

# Initialize sentinel variable
first_name = input("Enter first name of the first student or 'stop' to exit: ")

# Get input, update students list as list of lists
while first_name != 'stop':
    # Get input
    last_name = input("Enter last name of a student: ")
    exam_1_grade = input("Enter grades for exam # 1: ")
    exam_2_grade = input("Enter grades for exam # 2: ")
    exam_3_grade = input("Enter grades for exam # 3: ")
    # Update students list
    cur_student = [first_name, last_name, exam_1_grade, exam_2_grade, exam_3_grade]
    students.append(cur_student)
    # Ask for next student's data or 'stop' to exit
    first_name = input("Enter first name of the next student or 'stop' to exit: ")

# Display message how many students data will be processed
print(f"Data for {len(students)} students were processed and will be written into csv file.")

# Join data for individual students into a list of comma separated strings
students_as_strings = [','.join(student) + '\n' for student in students]

# Write into csv with writelines
with open("ex_09_03_grades_std.csv", mode='w') as fh_grades:
    fh_grades.writelines(students_as_strings)

# Write into csv with csv module and writerows
with open('ex_09_03_grades_csv.csv', mode='w', newline='') as fh_studs:
    writer = csv.writer(fh_studs)
    for row in students:
        writer.writerow(row)
