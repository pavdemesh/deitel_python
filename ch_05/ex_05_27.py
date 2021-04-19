"""
Use a list comprehension to create a list of 50 random values in the range 1 through 10.
Use NumPy’s unique function to obtain the unique values and their frequencies.
Display the results.
"""

import random
import numpy as np

# Generate list of 50 random ints in range(1, 11)
nums = [random.randrange(1, 11) for i in range(50)]

# Count frequencies using np.unique, store results in two ndarrays
unique_nums, unique_freqs = np.unique(nums, return_counts=True)

# Convert ndarrays with unique nums and their counts into lists
unique_nums = list(unique_nums)
unique_freqs = list(unique_freqs)

# Display results
for i in range(len(unique_nums)):
    print(f"Frequency of number {unique_nums[i]:>2} is: {unique_freqs[i]}")
