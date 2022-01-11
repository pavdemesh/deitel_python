# Exercise 10_09 from Deitel: Intro to Python and CS

"""
Write a class that implements a Square shape.
The class should contain a side property. Provide an __init__ method that takes the side length as an argument.
Also, provide the following read-only properties:
a) perimeter returns 4 × side.
b) area returns side × side.
c) diagonal returns the square root of the expression (2 × side2).
The perimeter, area and diagonal should not have corresponding data attributes;
rather, they should use side in calculations that return the desired values.
Create a Square object and display its side, perimeter, area and diagonal properties’ values.
"""


# Square class definition
class Square:
    """Square class for working with trigonometric functions on squares"""

    def __init__(self, side_length):
        """Initialize s Square object using side length."""
        self.side = side_length

    @property
    def side(self):
        """Return the side."""
        return self._side

    @side.setter
    def side(self, side_length):
        """Set the side length"""
        self._side = side_length

    @property
    def perimeter(self):
        """Return the perimeter."""
        return self.side * 4

    @property
    def area(self):
        """Return the area."""
        return self.side * self.side

    @property
    def diagonal(self):
        """Return the diagonal."""
        return pow(base=2, exp=0.5) * self.side


# Instantiate object of class Square
s1 = Square(10)
# Display its properties
print(f"Side length is: {s1.side}")
print(f'Perimeter is: {s1.perimeter}')
print(f'Area is: {s1.area}')
print(f'Diagonal is: {s1.diagonal:.2f}')
