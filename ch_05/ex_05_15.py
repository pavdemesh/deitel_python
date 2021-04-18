"""
Use tuples to represent hardware store invoices that consist of four pieces of data:
1) a part ID string, 2) a part description string, 3) an integer quantity of the item being purchased and,
4) a float item price.
"""


from operator import itemgetter


# List to hold invoice tuples
invoices = []

# Define invoice tuples
item1 = ("83", "Electric sander", 7, 57.98)
item2 = ("24", "Power saw", 18, 99.99)
item3 = ("7", "Sledge hammer", 11, 21.50)
item4 = ("77", "Hammer", 76, 11.99)
item5 = ("39", "Jig saw", 3, 79.50)

# Append invoice tuples to list
invoices.append(item1)
invoices.append(item2)
invoices.append(item3)
invoices.append(item4)
invoices.append(item5)

print("-------------------------------------------------------------------------------------------")

print("task a:")
# a-1) Use function sorted with a key argument to sort the tuples by part description
sorted_by_description = sorted(invoices, key=lambda x: x[1])
print(sorted_by_description)

# a-2) Use function sorted with a key argument and itemgetter to sort the tuples by part description
sorted_by_description_itemget = sorted(invoices, key=itemgetter(1))
print(sorted_by_description_itemget)

print("-------------------------------------------------------------------------------------------")

print("task b:")
# b-1) Use the sorted function with a key argument to sort the tuples by price
sorted_by_price = sorted(invoices, key=lambda x: x[3])
print(sorted_by_price)

# b-2) Use the sorted function with a key argument and itemgetter to sort the tuples by price
sorted_by_price_itemget = sorted(invoices, key=itemgetter(3))
print(sorted_by_price_itemget)

print("-------------------------------------------------------------------------------------------")

print("task c:")
# c) Map each invoice tuple to a tuple containing the part description and quantity & sort the results by quantity
description_plus_quantity = sorted([(x[1], x[2]) for x in invoices], key=itemgetter(1))
# Alternative using map()
description_plus_quantity_map = list(map(lambda x: (x[1], x[2]), invoices))
description_plus_quantity_map.sort(key=lambda x: x[1])
# Compare the results
print(description_plus_quantity)
print(description_plus_quantity_map)

print("-------------------------------------------------------------------------------------------")

print("task d:")
# d) Map each invoice tuple to a tuple containing the part description and the value of the invoice
# (the product of the quantity and the item price), sort the results by the invoice value.
description_plus_value = sorted([(x[1], round(x[2] * x[3], 2)) for x in invoices], key=lambda x: x[1])
print(description_plus_value)

print("-------------------------------------------------------------------------------------------")

print("task e:")
# e) Modify Part (d) to filter the results to invoice values in the range $200 to $500.
description_plus_value_filtered = sorted([(x[1], round(x[2] * x[3], 2)) for x in invoices], key=lambda x: x[1])
description_plus_value_filtered = list(filter(lambda x: 200 <= x[1] <= 500, description_plus_value_filtered))
print(description_plus_value_filtered)

print("-------------------------------------------------------------------------------------------")

print("task f")
# f) Calculate the total of all the invoices
total = sum(x[2] * x[3] for x in invoices)
print(f"Total of all invoices is: {total:.2f}")

print("-------------------------------------------------------------------------------------------")
