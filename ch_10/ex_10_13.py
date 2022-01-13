# Exercise 10_13 from Deitel: Intro to Python and CS

"""
Create a script containing the following maximum function

def maximum(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

Modify the docstring to define tests for calling function maximum with three ints, three floats and three strings.
For each type, provide three tests:
one with the largest value as the first argument, as the second argument, as the third argument.
Use doctest to run your tests and confirm that all execute correctly.
Next, modify the maximum function to use < operators rather than > operators.
Run your tests again to see which tests fail.
"""


def maximum(value1, value2, value3):
    """Return the maximum of three values.
    Testing for ints
    >>> maximum(4, 2, 3)
    4
    >>> maximum(2, 5, 3)
    5
    >>> maximum(2, 3, 6)
    6

    Now testing with flosts
    >>> maximum(5.2, 3.2, 4.16)
    5.2
    >>> maximum(3.2, 6.2, 4.16)
    6.2
    >>> maximum(5.2, 3.2, 8.16)
    8.16

    Now testing with strings
    >>> maximum('cccc', 'bbbb', 'aaaa')
    'cccc'
    >>> maximum('aaaa', 'cccc', 'bbbb')
    'cccc'
    >>> maximum('aaaa', 'bbbb', 'cccc')
    'cccc'
    """
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value


def maximum2(value1, value2, value3):
    """Return the maximum of three values.
    Testing for ints
    >>> maximum2(4, 2, 3)
    4
    >>> maximum2(2, 5, 3)
    5
    >>> maximum2(2, 3, 6)
    6

    Now testing with flosts
    >>> maximum2(5.2, 3.2, 4.16)
    5.2
    >>> maximum2(3.2, 6.2, 4.16)
    6.2
    >>> maximum2(5.2, 3.2, 8.16)
    8.16

    Now testing with strings
    >>> maximum2('cccc', 'bbbb', 'aaaa')
    'cccc'
    >>> maximum2('aaaa', 'cccc', 'bbbb')
    'cccc'
    >>> maximum2('aaaa', 'bbbb', 'cccc')
    'cccc'
    """
    max_value = value1
    if max_value < value2:
        max_value = value2
    if max_value < value3:
        max_value = value3
    return max_value


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
