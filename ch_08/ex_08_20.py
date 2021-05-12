# Exercise 08_20 from Deitel: Intro to Python and CS

"""
Dates are stored and displayed in several common formats. Three common formats are:
042555
04/25/1955
April 25, 1955

Use regular expressions to search a string containing dates, find substrings that match these formats
and munge them into the other formats.
The original string should have one date in each format, so there will be a total of six transformations.
"""

import re

# Get input from user
text_from_user = input("Enter string with numbers: ")
print()
print("------------------")

# Define three patterns
# Pattern 1: 042555
pattern1 = r"(\d{2})(\d{2})(\d{2})"

# Pattern 2: 04/25/1955
pattern2 = r"(\d{2})/(\d{2})/(\d{4})"

# Pattern 3: April 25, 1955
pattern3 = r"(\b[A-Z][a-z]+) (\d{2}), (\d{4})"

# Define dictionary to match month name and its number
month_to_num = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06",
                "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"}

# Define dictionary to match number and corresponding month name
num_to_month = {value: key for key, value in month_to_num.items()}


def find_transform_patt_1(text, patt=pattern1):
    """
    Finds date matching pattern 1 and prints 2 alternative formats for this date
    :param text: String
    :param patt: regexp
    :return: None (prints 2 alternative formats)
    """
    # Search string for this pattern
    res = re.search(pattern=patt, string=text)
    if res:
        print(f"Found the following date: {res.group()}")
        print("This date can be transformed into following formats:")
        alternative_1 = f"{res.group(1)}/{res.group(2)}/{19 if int(res.group(3)) > 22 else 20}{res.group(3)}"
        alternative_2 = f"{num_to_month[res.group(1)]} {res.group(2)}, " \
                        f"{19 if int(res.group(3)) > 22 else 20}{res.group(3)}"
        print(alternative_1)
        print(alternative_2)
        print("------------------")
        return
    print("No valid date of this format found!")


def find_transform_patt_2(text, patt=pattern2):
    """
    Finds date matching pattern 2 and prints 2 alternative formats for this date
    :param text: String
    :param patt: regexp
    :return: None (prints 2 alternative formats)
    """
    # Search string for this pattern
    res = re.search(pattern=patt, string=text)
    if res:
        print(f"Found the following date: {res.group()}")
        print("This date can be transformed into following formats:")
        alternative_1 = f"{res.group(1)}{res.group(2)}{res.group(3)[2:]}"
        alternative_2 = f"{num_to_month[res.group(1)]} {res.group(2)}, {res.group(3)}"
        print(alternative_1)
        print(alternative_2)
        print("------------------")
        return
    print("No valid date of this format found!")


def find_transform_patt_3(text, patt=pattern3):
    """
    Finds date matching pattern 3 and prints 2 alternative formats for this date
    :param text: String
    :param patt: regexp
    :return: None (prints 2 alternative formats)
    """
    # Search string for this pattern
    res = re.search(pattern=patt, string=text)
    if res:
        print(f"Found the following date: {res.group()}")
        print("This date can be transformed into following formats:")
        alternative_1 = f"{month_to_num[res.group(1)]}{res.group(2)}{res.group(3)[2:]}"
        alternative_2 = f"{month_to_num[res.group(1)]}/{res.group(2)}/{res.group(3)}"
        print(alternative_1)
        print(alternative_2)
        print("------------------")
        return
    print("No valid date of this format found!")


find_transform_patt_1(text_from_user)
find_transform_patt_2(text_from_user)
find_transform_patt_3(text_from_user)
