""" model class Rectangle
"""
from models.base import Base


class Rectangle(Base):

    """iniatialize class Rectangle."""

    # __width = width
    # __height = height
    # __x = x
    # __y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """call super with id"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
