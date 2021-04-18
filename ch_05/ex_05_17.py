"""
With regard to the following code:
a) How many times does the filter operation call its lambda argument? x 10
b) How many times does the map operation call its lambda argument? x 5
c) If you reverse filter() and map(), how many times does the map() call its lambda argument? x10
"""

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
# odds_squared = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))

counter_filter = 0
counter_map = 0


def is_odd(x):
    print("Running filter operation")
    global counter_filter
    counter_filter +=1
    return x % 2 != 0


def squared(x):
    print("Running map operation")
    global counter_map
    counter_map +=1
    return x ** 2


odds_squared = list(map(squared, filter(is_odd, numbers)))
print()
print("The output of these map() and filter() operations is the following list of squared odd values:")
print(odds_squared)
print()
print(f"Counter of map operations is: {counter_map}")
print(f"Counter of filter operations is: {counter_filter}")
