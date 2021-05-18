# Exercise 09_05 from Deitel: Intro to Python and CS

"""
Reimplement Exercise 9.3 using the json module to write the student information to the file in JSON format.
For this exercise, create a dictionary of student data in the following format:
gradebook_dict = {"students": [student1dictionary, student2dictionary, ...]}
Each dictionary in the list represents one student and contains the keys:
"first_name", "last_name", "exam1", "exam2" and "exam3",
which map to the values representing student’s first name (string), last name (string) and three exam scores (integers).
Output the gradebook_dict in JSON format to the file grades.json.
"""

import json

# Initialize list of dictionaries to store students data
students_list = list()

# Initialize dictionary to store gradebook
gradebook_dict = {}

# Initialize sentinel variable
first_name = input("Enter first name of the first student or 'stop' to exit: ")

# Get input, update students list as list of dictionaries
while first_name != "stop":
    # Get input
    last_name = input("Enter last name of a student: ")
    exam_1_grade = input("Enter grades for exam # 1: ")
    exam_2_grade = input("Enter grades for exam # 2: ")
    exam_3_grade = input("Enter grades for exam # 3: ")
    # Update students list
    cur_student = {"first_name": first_name, "last_name": last_name,
                   "exam1": exam_1_grade, "exam2": exam_2_grade, "exam3": exam_3_grade}

    students_list.append(cur_student)
    # Ask for next student"s data or "stop" to exit
    first_name = input("Enter first name of the next student or 'stop' to exit: ")

# Display message how many students data will be processed
print(f"Data for {len(students_list)} students were processed and will be written into JSON file.")

# Update gradebook dictionary
gradebook_dict["students"] = students_list

with open('ex_09_06_grades.json', mode='w') as fh_grades:
    json.dump(gradebook_dict, fh_grades)
