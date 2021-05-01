# Exercise 07_16 from Deitel: Intro to Python for CS

"""
Research and use NumPy’s tile function to
create a checkerboard pattern of dashes and asterisks.
"""

import numpy as np

arr = np.array((["*", "-"], ["-", "*"]))
board = np.tile(arr, (4, 4))
print(board)
