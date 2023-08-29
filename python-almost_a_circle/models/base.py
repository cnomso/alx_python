"""

"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Intialize a base

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        self.id = id

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
