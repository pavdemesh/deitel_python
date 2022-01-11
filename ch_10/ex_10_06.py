# Exercise 10_06 from Deitel: Intro to Python and CS

"""
A circle has a point at its center.
Create a class Point that represents an (x-y) coordinate pair
and provides x and y readwrite properties for the attributes _x and _y.
Include __init__ and __repr__ methods,
and a move method that receives x- and y-coordinate values and sets the Point’s new location.
Create a class Circle that has as its attributes _radius and _point
(a Point that represents the Circle’s center location).
Include __init__ and __repr__ methods,
and a move method that receives x- and y-coordinate values
and sets a new location for the Circle by calling the composed Point object’s move method.
Test your Circle class:
Create a Circle object, display its string representation, move the Circle and display its string representation again.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


# Defining class Circle
class Circle:
    def __init__(self, x_center, y_center, radius):
        self._radius = radius
        self._point = Point(x_center, y_center)

    def move(self, new_x, new_y):
        # Move the center by using Point method 'move' on the self._point object of type Point
        self._point.move(new_x, new_y)

    def __repr__(self):
        return f"Circle(x_center={self._point.x}, y_center={self._point.y}, radius={self._radius})"


# Testing functionality of the class Point
# Create an instance of class point and print it
p1 = Point(15, 25)
print('Current point is: ' + str(p1))

# Move the point and print to check
p1.move(18, 29)
print('Point after move is: ' + str(p1))

# Test read-accessing individual properties
print(f'Value of x is: {p1.x}')

# Test write-accessing individual properties
p1.y = 1
print(f'Value of y after change is: {p1.y}')
print('-----------------------------------')

# Testing functionality of the class Circle
# Create an object of class Circle and print it
c1 = Circle(x_center=15, y_center=30, radius=50)
print('Current circle location is: ' + str(c1))

# Move the center of the Circle and print updated Circle
c1.move(25, 35)
print('Updated  circle location is: ' + str(c1))

# Accessing individual attributes of the self._point as object of type Point
print(f"The x coordinate of the circle's center is: {c1._point.x}")
