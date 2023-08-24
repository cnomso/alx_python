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
            raise TypeError('<name> must be an integer')
        elif value <=0:
            raise ValueError('<name> must be greater than 0')
    