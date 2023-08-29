""" model class Rectangle
"""
from models.base import Base


class Rectangle(Base):

    """iniatialize class Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """call super with id"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        __width = width
        __height = height
        __x = x
        __y = y

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of Rectangle instance."""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle."""
        # for _ in range(self.height):
        #     print("#" * self.width)
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns print() and str() of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args):
        """Update the Rectangle."""

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
