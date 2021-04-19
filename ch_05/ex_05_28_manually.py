"""
Twenty students were asked to rate on a scale of 1 to 5 the quality of the food in the student cafeteria,
1 being “awful” and 5 being “excellent.” Place the 20 responses in a list
1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5
Determine and display the frequency of each rating.
Use the built-in functions, statistics module functions and NumPy functions demonstrated in Section 5.17.2 to display:
minimum, maximum, range, mean, median, mode, variance and standard deviation.
"""

import statistics as stats
import numpy as np

students_responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

ratings_minimum = min(students_responses)
ratings_maximum = max(students_responses)
print(f"Minimum is:".ljust(15), end="")
print(f"{ratings_minimum}")
print(f"Maximum is:".ljust(15), end="")
print(f"{ratings_maximum}")

# Calculate mean
ratings_mean = round(sum(students_responses) / len(students_responses), 2)
print(f"Mean is:".ljust(15), end="")
print(f"{ratings_mean}")

# Calculate median
if len(students_responses) % 2 == 1:
    ratings_median = sorted(students_responses)[len(students_responses) // 2]
    print(f"Median is: {ratings_median}")
else:
    index1 = len(students_responses) // 2
    index2 = len(students_responses) // 2 - 1
    ratings_median = round((sorted(students_responses)[index1] + sorted(students_responses)[index2]) / 2, 2)
    print(f"Median is:".ljust(15), end="")
    print(f"{ratings_median}")

# Calculate mode
# Get unique ratings and their frequencies both as ndarrays
rating_values, rating_frequencies = np.unique(students_responses, return_counts=True)
rating_values = list(rating_values)
rating_frequencies = list(rating_frequencies)

# If only one most frequent value - get its index and use it as to get corresponding rating from values
ratings_mode = "Mode can not be calculated."
if rating_frequencies.count(max(rating_frequencies)) == 1:
    ratings_mode = rating_values[rating_frequencies.index(max(rating_frequencies))]
print("Mode is: ".ljust(15), end="")
print(f"{ratings_mode}")

# Calculate population variance
ratings_pvariance = round(sum([(x-ratings_mean) ** 2 for x in students_responses]) / len(students_responses), 2)
print(f"Variance is:".ljust(15), end="")
print(f"{ratings_pvariance}")

# calculate standard deviation
ratings_stp_deviation = round(ratings_pvariance ** 0.5, 2)
print(f"Deviation is:".ljust(15), end="")
print(f"{ratings_stp_deviation}")
