# Exercise 09_02 from Deitel: Intro to Python and CS

"""
Write code that reads the grades from the grades.txt file you created in the previous exercise.
Display the individual grades and their total, count and average.
"""

# Initialize the total accumulator and the counter for grades
sum_grades = 0
count_grades = 0

with open("ex_09_01_grades.txt", mode='r') as fh_grades:
    for grade in fh_grades:
        grade = int(grade.strip())
        count_grades += 1
        print("Grade No. {count} is: {value}".format(count=count_grades, value=grade))
        sum_grades += grade


print("The total sum of grades is: {total}".format(total=sum_grades))
print("The total count of grades is: {count}".format(count=count_grades))
print("the average grade is: {average:.2f}".format(average=sum_grades / count_grades))
