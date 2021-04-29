# Exercise 07_08 from Deitel: Intro to Python for CS

"""
DataFrames are displayed in an attractive column-based format with row and column labels.
The values within each column are right aligned in the same field width,
which is determined by that column’s widest value.
To understand how powerful it is to have this formatting built-in,
write a function that reimplements DataFrame formatting using loops.
Assume the DataFrame contains only positive integer values
and that both the row and column labels are each integer values beginning at 0.
"""

import pandas as pd


def display_dataframe(df):
    """
    Reimplements DataFrame’s formatting using loops
    :param df: DataFrame with both the row and column labels as integers values beginning at 0
    :return: Prints out the DataFrame using loops
    """
    # Calculate longest int in ech column and store its length in a dictionary along with col_num
    col_widths = dict()
    for i in range(df.shape[1]):
        col_widths[i] = len(str(max(df.iloc[:, i])))

    # Print column indices
    # Account for 3 additional spaces at the beginning of each row (row index in field of 3)
    print("   ", end="")
    for i in range(df.shape[1]):
        print(f"{i:>{col_widths[i]}}", end="  ")
    print()

    # Print row indices followed by row content
    for row in range(df.shape[0]):
        print(f"{row:<3}", end="")
        for col in range(df.shape[1]):
            print(f"{df.at[row, col]:>{col_widths[col]}}", end="  ")
        print()


# Create DataFrame from dictionary
my_dict = {0: [13434, 2354665654436, 2, 2423525], 1: [64, 567444465, 2, 432356], 2: [87653, 54657876, 4325647, 432]}
my_df = pd.DataFrame(my_dict)

# Print using DataFrame functionality
print("This is DataFrame object's display via built-in functionality:")
print(my_df)
print()

# Print using custom function
print("This is DatFrame object's display via custom function:")
display_dataframe(my_df)
