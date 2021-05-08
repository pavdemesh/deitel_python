"""
Display every word that start with a "t" in the given string.
"""

# Get input and provide default input
s = input()
if len(s) == 0:
    s = "to beto or not to be that is the abc"

word = ""
previous = " "

for i, char in enumerate(s):
    # If we encounter any char other than "t" and are not working on a word
    if char != "t" and len(word) < 1:
        pass
    elif char != " " and len(word) >= 1:
        word += char
    elif char == " " and len(word) >= 1:
        print(word)
        word = ""
    elif char == "t" and previous == " ":
        word += char
    previous = s[i]

if len(word) > 0:
    print(word)
