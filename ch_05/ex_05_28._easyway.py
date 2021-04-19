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

# Get unique ratings and their frequencies both as ndarrays
rating_values, rating_frequencies = np.unique(students_responses, return_counts=True)

rating_values = list(rating_values)
rating_frequencies = list(rating_frequencies)

minimum_rating = min(rating_values)
maximum_rating = max(rating_values)
print(minimum_rating)
print(maximum_rating)

ratings_mean = stats.mean(students_responses)
print(ratings_mean)
ratings_median = stats.median(students_responses)
print(ratings_median)
ratings_mode = stats.mode(students_responses)
print(ratings_mode)

ratings_pvariance = stats.pvariance(students_responses)
print(ratings_pvariance)

rating_st_deviation = stats.pstdev(students_responses)
print(f"{round(rating_st_deviation, 2)}")
