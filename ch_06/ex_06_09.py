"""
Using the following dictionary, which maps country names to Internet top-level domains (TLDs):
tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
perform the following tasks and display the results:
"""

tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

print("--------------------------------------")

# a) Check whether the dictionary contains the key 'Canada'.
print("Task a): Check whether the dictionary contains the key 'Canada'.")
print(f"Key 'Canada' is in dictionary: {'Canada' in tlds}")
print("--------------------------------------")

# b) Check whether the dictionary contains the key 'France'.
print(f"Task b): Check whether the dictionary contains the key 'France'.")
print(f"Key 'France' is in dictionary: {'France' in tlds}")
print("--------------------------------------")

# c) Iterate through the key–value pairs and display them in two-column format.
print("Task c): Iterate through the key–value pairs and display them in two-column format.")
for country, code in tlds.items():
    print(f"{country:<15}{code}")
print("--------------------------------------")

# d) Add the key–value pair 'Sweden' and 'sw' (which is incorrect).
print("Task d): Add the key–value pair 'Sweden' and 'sw' (which is incorrect).")
tlds.update(Sweden='sw')
print(*tlds.items())
print("--------------------------------------")

# e) Update the value for the key 'Sweden' to 'se'.
print("Task e): Update the value for the key 'Sweden' to 'se'.")
tlds['Sweden'] = 'se'
print(*tlds.items())
print("--------------------------------------")

# f) Use a dictionary comprehension to reverse the keys and values.
print("Task f): Use a dictionary comprehension to reverse the keys and values.")
reversed_dict = {code: country for country, code in tlds.items()}
print(*reversed_dict.items())
print("--------------------------------------")

# g) With the result of part (f), use a dictionary comprehension to convert the country names to all uppercase letters.
print("Task g): With results of (f), use dictionary comprehension to convert country names to all uppercase.")
reversed_upper = {key:value.upper() for key, value in reversed_dict.items()}
print(*reversed_upper.items())
print("--------------------------------------")

