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
        print("[Rectangle] {}/{}".format(self.width , self.height))
        
    def area(self):
        return  "{}".format(self.width * self.height)
        
       
class Square(Rectangle):
    '''' rectangle class
        raise exceptions
    '''
    def __init__(self, size):
        self.size = size
        # self.integer_validator("size", size)

        print("[Rectangle] {}/{}".format(self.size , self.size))
        
    def area(self):
        return  "{}".format(self.size * self.size)
