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
        self.__width = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be >= 0".format(value))

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be >= 0".format(value))

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(value))
        if value < 0:
            raise ValueError("{} must be >= 0".format(value))

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(value))
        if value < 0:
            raise ValueError("{} must be >= 0".format(value))
