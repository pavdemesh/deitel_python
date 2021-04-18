"""
Define a function named display_table that receives a two-dimensional list and displays its contents in tabular format.
List the column indices as headings across the top, and list the row indices at the left of each row.
"""


def display_table(table: list):
    # Determine number of rows and columns in the table and store them in corresponding vars
    num_rows = len(table)
    num_cols = len(table[0])

    # Determine the padding by finding longest element in table and adding 3 to its length
    max_len = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if len(str(table[row][col])) > max_len:
                max_len = len(str(table[row][col]))
    padding = max_len + 3

    print(" ", end="")

    for i in range(num_cols):
        print(str(i).rjust(padding, " "), end="")
    print("\n")

    for row in range(num_rows):
        print(row, end="")
        for col in range(num_cols):
            print(str(table[row][col]).rjust(padding, " "), end="")
        print("\n")


my_table = [[2, 3, 4, 5], [8, 8, 8, 8], [9, 9, 9, 9], [11, 11, 11, 11], ["asha", 12, "mashup", True]]
display_table(my_table)
