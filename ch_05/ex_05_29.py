"""
Using the list in Exercise 5.28 and the techniques you learned in Section 5.17.2:
display a bar chart showing the response frequencies and their percentages of the total responses.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

students_responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

# Get unique ratings and their frequencies both as ndarrays
rating_values, rating_frequencies = np.unique(students_responses, return_counts=True)

# Define whitegrid and plot my chart
sns.set_style("whitegrid")
my_chart = sns.barplot(x=rating_values, y=rating_frequencies, palette="bright")

# Add title
chart_title = "Evaluation of Cafeteria by Students"
my_chart.set_title(chart_title)

# Add labels for x and y axes
my_chart.set(xlabel='Ratings', ylabel='Frequency')

# Add space above to accommodate text for each patch
my_chart.set_ylim(top=max(rating_frequencies) * 1.10)

for bar, frequency in zip(my_chart.patches, rating_frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text_above_bar = f"{frequency}\n{frequency / len(students_responses):.1%}"
    my_chart.text(text_x, text_y, text_above_bar, fontsize=11, ha="center", va="bottom")

plt.show()
