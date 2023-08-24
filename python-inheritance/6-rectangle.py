'''' BaseGeometry class
'''

class BaseGeometry:
    '''' Geometry class
        raise exptions
    '''
    
    def __init__(self):
        pass

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError('{} must be an integer' .format(name))
        elif value <=0:
            raise ValueError('{} must be greater than 0' .format(name))

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def integer_validator(self, width, height):

        '''' rectangle class
        raise exceptions
        '''
        # self.name = name
        # self.value = value
        self.width = width
        self.height = height

        # if type(width) is not int:
        #     raise TypeError('{} must be an integer' .format(width))
        if type(height) is not int:
            raise TypeError('{} must be an integer' .format(name))
           
    