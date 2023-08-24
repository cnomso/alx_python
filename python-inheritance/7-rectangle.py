'''' 
BaseGeometry class
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
    '''' rectangle class
        raise exceptions
    '''
    
    def __init__(self, width, height):
        
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
        
    def area(self):
        return  "[Rectangle] {}/{}".format(self.width, self.height)
        
       
    
    def str(self):
        return "[Rectangle] {}/{}".format(self.width, self.height)
    