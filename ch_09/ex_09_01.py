# Exercise 09_01 from Deitel: Intro to Python and CS

"""
Figure 3.2 presented a class_average script in which you could enter any number of grades followed by a sentinel value,
then calculate the class average. Another approach would be to read the grades from a file.
Write code that enables you to store any number of grades into a grades.txt plain text file.
"""

with open("ex_09_01_grades.txt", mode='w') as fh_grades:
    grade = input("Enter a grade or 'stop' to exit: ")
    while grade != "stop":
        fh_grades.write(grade+'\n')
        grade = input("Enter next grade or 'stop' to exit: ")

print("Finished writing grades to the file.")
