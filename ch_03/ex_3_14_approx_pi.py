"""Compute the value of pi from following infinite series:
pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 ...
Print result for each term"""

# Initialize variables
pi = 4
subtract_term = True
denominator = 3

for i in range(200000):
    if subtract_term:
        pi = pi - 4/denominator
    elif not subtract_term:
        pi = pi + 4/denominator
    # print(f"For term number {i + 1} and denominator {denominator} the value of pi is: {pi}")
    subtract_term = not subtract_term
    denominator += 2

print(f"Final value of pi is: {pi}")
