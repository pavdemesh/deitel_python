# Exercise 10_10 from Deitel: Intro to Python and CS

"""
Create a class called Invoice that a hardware store might use to represent an invoice for an item sold at the store.
An Invoice should include four pieces of information as data attributes:
a part number (a string), a part description (a string), a quantity of the item being purchased (an int)
and a price per item (a Decimal). Your class should have an __init__ method that initializes the four data attributes.
Provide a property for each data attribute.
The quantity and price per item should each be non-negative -
use validation in the properties for these data attributes to ensure that they remain valid.
Provide a calculate_invoice method that returns the invoice amount (multiplies the quantity by the price per item).
Demonstrate class Invoice’s capabilities.
"""

from decimal import Decimal


class Invoice:
    """Class Invoice to work with invoices"""

    def __init__(self, part_number, part_descript, item_quantity, item_price):
        self.part_number = part_number
        self.part_descript = part_descript
        self.item_price = item_price
        self.item_quantity = item_quantity

    @property
    def part_number(self):
        """Return the part number."""
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Set the part number."""
        self._part_number = part_number

    @property
    def part_descript(self):
        """Return the part description."""
        return self._part_descript

    @part_descript.setter
    def part_descript(self, part_descript):
        """Set the part description."""
        self._part_descript = part_descript

    @property
    def item_quantity(self):
        """Return the item quantity."""
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, item_quantity):
        """Set the item quantity."""
        # if quantity is less than 0, raise an Error
        if item_quantity < 0:
            raise ValueError("Quantity must be >= 0.")
        # Set item quantity
        self._item_quantity = item_quantity

    @property
    def item_price(self):
        """Return the item price."""
        return self._item_price

    @item_price.setter
    def item_price(self, item_price):
        """Set the item price."""
        # if price is less than 0, raise an Error
        if item_price < Decimal('0.00'):
            raise ValueError("Price must be >= 0.00.")
        # Set item price
        self._item_price = item_price

    def calculate_invoice(self):
        """Calculate the invoice amount"""
        return self.item_price * self.item_quantity


# Create object with correct data
inv1 = Invoice(part_number='123-333-456', part_descript="Hammer", item_quantity=11, item_price=Decimal('22.14'))

# Test reading and writing attributes
print(f'Item price should be 22.14: {inv1.item_price}')
print(f'Part description should be "Hammer": {inv1.part_descript}')

# Change part number
inv1.part_number = '333-333-333'
print(f"Updated part number should be 333-333-333: {inv1.part_number}")

# Test setting negative value for item quantity
try:
    inv1.item_quantity = -4
except ValueError:
    print("Check successful. Was unable to set item quantity to a negative value")

# Calculate invoice amount
invoice_amount = inv1.calculate_invoice()
print(f"Invoice amount should be 243.54: {invoice_amount}")
