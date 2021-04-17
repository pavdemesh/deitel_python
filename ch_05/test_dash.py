
fh = open("words_small.txt", "r")
# Create empty list to store legit words
legit_words = []

# Iterate over txt dictionary file line by line and append to legit_words if the word is legit
for word in fh:
    word = word.lower().strip()
    mytable = word.maketrans("y", "y", "-")
    print(word.translate(mytable))

#     # Filter out words of length other than 7
#     if len(word) != 7 or len(word.strip("-")) != 7:
#         continue
#         # Additional check for words of desired_length: must consist only of chars except q and z plus dash
#     else:
#         is_legit = True
#         for char in word:
#             if char not in "abcdefghijklmnoprstuvwxy-":
#                 is_legit = False
#                 break
#         if is_legit:
#             legit_words.append(word)
#
# print(legit_words)