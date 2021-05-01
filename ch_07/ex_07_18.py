# Exercise 07_18 from Deitel: Intro to Python for CS

"""
NumPy arrays offer a mean method, but not median or mode.
Write functions median and mode that use existing NumPy capabilities:
Determine the median (middle) and mode (most frequent) of the values in an array.
Your functions should determine the median and mode regardless of the array’s shape.
Test your function on three arrays of different shapes.
"""

import numpy as np
import statistics as st


def custom_median(arr):
    """
    Determines median value of an ndarray regardless of its shape.
    :param arr: NumPy array of ints or floats
    :return: Median (middle value in sorted array)
    """
    arr_flattened = arr.flatten()
    arr_sorted = np.sort(arr_flattened)

    # If odd number of elements - return middle
    if arr_sorted.size % 2 == 1:
        mid = arr_sorted.size // 2
        return arr_sorted[mid]
    # Else (even number of items) - return average of two middle elements
    else:
        mid = arr_sorted.size // 2
        return (arr_sorted[mid] + arr_sorted[mid - 1]) / 2


def custom_mode(arr):
    """
    Determines mode of an ndarray regardless of its shape.
    :param arr: NumPy array of ints or floats
    :return: Mode (most frequent value in sorted array)
    """
    # Keep track of frequencies using dictionary functionality
    freqs = dict()

    # Create flattened copy of the array
    arr_flattened = arr.flatten()

    # Iterate over elements in flattened array and update frequencies
    for number in arr_flattened:
        freqs[number] = freqs.get(number, 0) + 1

    # Determine highest frequency:
    highest_frequency = max(list(freqs.values()))

    # Create list to hold mode(s)
    list_of_modes = list()
    for num, count in freqs.items():
        if count == highest_frequency:
            list_of_modes.append(num)

    # If only one item with highest occurrence frequency in the list of modes - return it
    if len(list_of_modes) == 1:
        return list_of_modes[0]
    # Else - return the mode value which occurs first in the ndarray
    else:
        # Iterate over index and number through the list of modes
        for i, num in enumerate(list_of_modes):
            # Convert every item in the list into a tuple containing mode value and its index in the original array
            list_of_modes[i] = (num, np.where(arr_flattened == num)[0][0])
        # Return first value in the list of (mode, index) tuples sorted by index
        # It will be mode value with lowest index and thus mode value that occurs first
        return sorted(list_of_modes, key=lambda x: x[1])[0][0]


def test_custom_median(arr1, arr2, arr3):
    """
    Tests custom_median() function with 3 different test arrays
    :param arr1: Test array 1
    :param arr2: Test array 2
    :param arr3: test array 3
    :return: Print "passed" or "failed" for each test
    """
    print("--------------------------------------------")
    print("Testing custom_median() function on 3 arrays:")
    # Test case 1
    print(f"Test case #1: {arr1.ndim}D array of shape: {arr1.shape}")
    if custom_median(arr1) == st.median(list(arr1.flatten())):
        print("Test 1 PASSED !")
    else:
        print("Test 1 FAILED !")

    # Test case 2
    print(f"Test case #2: {arr2.ndim}D array of shape: {arr2.shape}")
    if custom_median(arr2) == st.median(list(arr2.flatten())):
        print("Test 2 PASSED !")
    else:
        print("Test 2 FAILED !")

    # Test case 3
    print(f"Test case #3: {arr3.ndim}D array of shape: {arr3.shape}")
    if custom_median(arr3) == st.median(list(arr3.flatten())):
        print("Test 3 PASSED !")
    else:
        print("Test 3 FAILED !")

    print()


def test_custom_mode(arr1, arr2, arr3):
    """
    Tests custom_mode() function with 3 different test arrays
    :param arr1: Test array 1
    :param arr2: Test array 2
    :param arr3: test array 3
    :return: Print "passed" or "failed" for each test
    """
    print("--------------------------------------------")
    print("Testing custom_mode() function on 3 arrays:")

    # Test case 1
    print(f"Test case #1: {arr1.ndim}D array of shape: {arr1.shape}")
    if custom_mode(arr1) == st.mode(list(arr1.flatten())):
        print("Test 1 PASSED !")
    else:
        print("Test 1 FAILED !")

    # Test case 2
    print(f"Test case #2: {arr2.ndim}D array of shape: {arr2.shape}")
    if custom_mode(arr2) == st.mode(list(arr2.flatten())):
        print("Test 2 PASSED !")
    else:
        print("Test 2 FAILED !")

    # Test case 3
    print(f"Test case #3: {arr3.ndim}D array of shape: {arr3.shape}")
    if custom_mode(arr3) == st.mode(list(arr3.flatten())):
        print("Test 3 PASSED !")
    else:
        print("Test 3 FAILED !")

    print()


# Test arrays for custom_median()
test_arr1 = np.random.randint(low=0, high=100, size=(7, 3))
test_arr2 = np.linspace(1, 30, 16).reshape(4, 4)
test_arr3 = np.random.randint(low=0, high=1000, size=(4, 6, 5))

# Test arrays for custom_mode()
rpt_arr1 = np.random.randint(low=0, high=100, size=(14, 14))
rpt_arr2 = np.random.randint(low=0, high=1000, size=(30, 30, 30))
rpt_arr3 = np.random.randint(low=0, high=500, size=(11, 11, 11, 11))

# Running tests
test_custom_median(test_arr1, test_arr2, test_arr3)
test_custom_mode(rpt_arr1, rpt_arr2, rpt_arr3)
