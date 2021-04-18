
def is_sorted(seq):
    """
    Receives a sequence and returns True if the elements are in sorted order.
    :param seq: list, tuple or string
    :return: True if sorted, else False
    """
    for i in range(len(seq) - 1):
        if seq[i] > seq[i+1]:
            return False
    return True


test_case_1 = "abcdefg"
test_case_2 = "abcdefa"

test_case_3 = (3, 4, 5, 6, 7, 8)
test_case_4 = (5, 6, 7, 3)

print("Correct output must be: True, False, True, False")

print(is_sorted(test_case_1))
print(is_sorted(test_case_2))
print(is_sorted(test_case_3))
print(is_sorted(test_case_4))
