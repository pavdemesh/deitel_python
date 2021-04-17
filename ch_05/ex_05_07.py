def unique_sorted(sequence):
    """
    Receives a list
    Returns a (possibly shorter) list with only unique values in sorted order.
    """
    unique_sorted_list = list()
    for item in sequence:
        if item in unique_sorted_list:
            continue
        else:
            unique_sorted_list.append(item)
    unique_sorted_list.sort()
    return unique_sorted_list
    

nonsorted_nonunique_nums = [2, 2, 2, 5, 5, 3, 3, 2, 2, 7, 6, 6, 6]

nonsorted_nonunique_string = "mama myla ramu papu bili v rylo"

print(unique_sorted(nonsorted_nonunique_nums))
print(unique_sorted(nonsorted_nonunique_string))
  
