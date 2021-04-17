import string

alphabet = string.ascii_lowercase

# Print first half
print(alphabet[0:len(alphabet)//2 + 1])
print(alphabet[:len(alphabet)//2 + 1])

# Print second half
print(alphabet[len(alphabet) // 2 + 1: len(alphabet)])
print(alphabet[len(alphabet) // 2 + 1:])

# Print every second letter
print(alphabet[::2])

# Print in reversed order
print(alphabet[::-1])
print(alphabet[len(alphabet)-1::-1])
print(alphabet[-1:-(len(alphabet) + 1): -1])

# Print every third letter in reversed string
print(alphabet[::-1][::3])



