# Exercise 07_19 from Deitel: Intro to Python for CS

"""
Modify your functions from 07_18.py to allow the user to provide an axis keyword argument
so the calculations can be performed row-by-row or column-by-column on a two-dimensional array.
"""

import numpy as np
import statistics as st


def mode_1d_array(arr):
    """
    Determines mode (most frequent) value of an 1D (flat) ndarray.
    :param arr: NumPy 1D array of ints or floats
    :return: A ndarray containing mode (most frequent value in sorted array) for 1D ndarray
    """
    # Keep track of frequencies using dictionary functionality
    freqs = dict()

    # Iterate over elements in flattened array and update frequencies
    for number in arr:
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
        return np.array([list_of_modes[0]])
    # Else - return the mode value which occurs first in the ndarray
    else:
        # Iterate over index and number through the list of modes
        for i, num in enumerate(list_of_modes):
            # Convert every item in the list into a tuple containing mode value and its index in the original array
            list_of_modes[i] = (num, np.where(arr == num)[0][0])
        # Return first value in the list of (mode, index) tuples sorted by index
        # It will be mode value with lowest index and thus mode value that occurs first
        return np.array([sorted(list_of_modes, key=lambda x: x[1])[0][0]])


def custom_median(arr, axis='row'):
    """
    Determines median value of 2D ndarray row-by-row or column-by-column.
    :param arr: NumPy array of ints or floats
    :param axis: String 'row' or 'col' to get median row-by-row or col-by-col. 'row' is default
    :return: A ndarray of median (middle value in sorted array) row-by-row or col-by-col
    """
    # Create list to hold medians
    medians = list()

    # Calculate median row-by-row
    if axis == 'row':
        # Iterate over rows of the arr
        for row_ind in range(arr.shape[0]):
            row_sorted = np.sort(arr[row_ind])
            # If odd number of elements - add middle element to medians list
            if row_sorted.size % 2 == 1:
                mid = row_sorted.size // 2
                medians.append(float(row_sorted[mid]))
            # Else (even number of items) - return average of two middle elements
            else:
                mid = row_sorted.size // 2
                medians.append((row_sorted[mid] + row_sorted[mid - 1]) / 2)
    # Elif axis is 'col' - do the same col-by-col
    elif axis == 'col':
        # Iterate over cols of the arr
        for col_ind in range(arr.shape[1]):
            col_sorted = np.sort(arr[:, col_ind])
            # If odd number of elements - add middle element to medians list
            if col_sorted.size % 2 == 1:
                mid = col_sorted.size // 2
                medians.append(float(col_sorted[mid]))
            # Else (even number of items) - return average of two middle elements
            else:
                mid = col_sorted.size // 2
                medians.append((col_sorted[mid] + col_sorted[mid - 1]) / 2)

    return np.array(medians)


def custom_mode(arr, axis='row'):
    """
    Determines mode (most frequent) values of an ndarray row-by-row or column-by-column.
    :param arr: NumPy array of ints or floats
    :param axis: String 'row' or 'col' to get modes row-by-row or col-by-col. 'row' is default
    :return: A ndarray of modes (most frequent value in sorted array) row-by-row or col-by-col
    """
    # Create list to store modes for row resp. columns
    modes = np.array([])

    # Calculate median row-by-row
    if axis == 'row':
        # Iterate over rows of the arr
        for row_ind in range(arr.shape[0]):
            modes = np.concatenate((modes, mode_1d_array(arr[row_ind])))

    # Elif axis is 'col' - do the same col-by-col
    elif axis == 'col':
        # Iterate over cols of the arr
        for col_ind in range(arr.shape[1]):
            modes = np.concatenate((modes, mode_1d_array(arr[:, col_ind])))

    return modes


def test_custom_median(arr1, arr2, arr3):
    """
    Tests custom_median() function with 3 different test arrays
    :param arr1: Test array 1
    :param arr2: Test array 2
    :param arr3: test array 3
    :return: Print "passed" or "failed" for each test
    """
    print("--------------------------------------------")
    print("Testing custom_median() function on 3 arrays for both axes:")
    # Test case 1
    print(f"Test case #1: {arr1.ndim}D array of shape: {arr1.shape}")
    # Check correctness of median for rows and columns
    has_passed_on_rows = all(custom_median(arr1, axis='row') == np.median(arr1, 1))
    has_passed_on_cols = all(custom_median(arr1, axis='col') == np.median(arr1, 0))
    # Display result
    if has_passed_on_cols and has_passed_on_rows:
        print("Test 1 PASSED !")
    else:
        print("Test 1 FAILED !")

    # Test case 2
    print(f"Test case #2: {arr2.ndim}D array of shape: {arr2.shape}")
    # Check correctness of median for rows and columns
    has_passed_on_rows = all(custom_median(arr2, axis='row') == np.median(arr2, 1))
    has_passed_on_cols = all(custom_median(arr2, axis='col') == np.median(arr2, 0))
    # Display result
    if has_passed_on_cols and has_passed_on_rows:
        print("Test 2 PASSED !")
    else:
        print("Test 2 FAILED !")

    # Test case 3
    print(f"Test case #3: {arr3.ndim}D array of shape: {arr3.shape}")
    # Check correctness of median for rows and columns
    has_passed_on_rows = all(custom_median(arr3, axis='row') == np.median(arr3, 1))
    has_passed_on_cols = all(custom_median(arr3, axis='col') == np.median(arr3, 0))
    # Display result
    if has_passed_on_cols and has_passed_on_rows:
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
    print("Testing custom_mode() function on 3 arrays for both axes:")

    # Test case 1
    print(f"Test case #1: {arr1.ndim}D array of shape: {arr1.shape}")
    # Calculate modes by row and col using custom_mode function
    modes_by_row_custom = custom_mode(arr1, axis='row')
    # print(modes_by_row_custom)
    modes_by_col_custom = custom_mode(arr1, axis='col')
    # print(modes_by_col_custom)

    # Calculate modes by row and col using statistics module
    modes_by_row_stats = np.array([float(st.mode(list(arr1[i]))) for i in range(arr1.shape[0])])
    # print(modes_by_row_stats)
    modes_by_col_stats = np.array([float(st.mode(list(arr1[:, i]))) for i in range(arr1.shape[1])])
    # print(modes_by_col_stats)

    # Check correctness of modes for rows and columns
    has_passed_on_rows = all(modes_by_row_custom == modes_by_row_stats)
    has_passed_on_cols = all(modes_by_col_custom == modes_by_col_stats)

    # Display result
    if has_passed_on_cols and has_passed_on_rows:
        print("Test 1 PASSED !")
    else:
        print("Test 1 FAILED !")

    # Test case 2
    print(f"Test case #2: {arr2.ndim}D array of shape: {arr2.shape}")
    # Calculate modes by row and col using custom_mode function
    modes_by_row_custom = custom_mode(arr2, axis='row')
    # print(modes_by_row_custom)
    modes_by_col_custom = custom_mode(arr2, axis='col')
    # print(modes_by_col_custom)

    # Calculate modes by row and col using statistics module
    modes_by_row_stats = np.array([float(st.mode(list(arr2[i]))) for i in range(arr2.shape[0])])
    # print(modes_by_row_stats)
    modes_by_col_stats = np.array([float(st.mode(list(arr2[:, i]))) for i in range(arr2.shape[1])])
    # print(modes_by_col_stats)

    # Check correctness of modes for rows and columns
    has_passed_on_rows = all(modes_by_row_custom == modes_by_row_stats)
    has_passed_on_cols = all(modes_by_col_custom == modes_by_col_stats)

    # Display result
    if has_passed_on_cols and has_passed_on_rows:
        print("Test 1 PASSED !")
    else:
        print("Test 1 FAILED !")

    # Test case 3
    print(f"Test case #3: {arr3.ndim}D array of shape: {arr3.shape}")
    # Calculate modes by row and col using custom_mode function
    modes_by_row_custom = custom_mode(arr3, axis='row')
    # print(modes_by_row_custom)
    modes_by_col_custom = custom_mode(arr3, axis='col')
    # print(modes_by_col_custom)

    # Calculate modes by row and col using statistics module
    modes_by_row_stats = np.array([float(st.mode(list(arr3[i]))) for i in range(arr3.shape[0])])
    # print(modes_by_row_stats)
    modes_by_col_stats = np.array([float(st.mode(list(arr3[:, i]))) for i in range(arr3.shape[1])])
    # print(modes_by_col_stats)

    # Check correctness of modes for rows and columns
    has_passed_on_rows = all(modes_by_row_custom == modes_by_row_stats)
    has_passed_on_cols = all(modes_by_col_custom == modes_by_col_stats)

    # Display result
    if has_passed_on_cols and has_passed_on_rows:
        print("Test 1 PASSED !")
    else:
        print("Test 1 FAILED !")

    print()


# Test arrays for custom_median()
test_arr1 = np.random.randint(low=0, high=100, size=(7, 3))
test_arr2 = np.linspace(1, 30, 16).reshape(4, 4)
test_arr3 = np.random.randint(low=0, high=1000, size=(20, 30))

# Test arrays for custom_mode()
rpt_arr1 = np.random.randint(low=0, high=70, size=(14, 9))
rpt_arr2 = np.random.randint(low=0, high=300, size=(32, 91))
rpt_arr3 = np.random.randint(low=0, high=50, size=(12, 13))

# Running tests
test_custom_median(test_arr1, test_arr2, test_arr3)
test_custom_mode(rpt_arr1, rpt_arr2, rpt_arr3)
