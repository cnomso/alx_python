''' class of square
    creates private size
'''
class Square():
    ''' instantiate size
    private attribute: size
    square the size
    '''
    def __init__(self, size=0):
        self._Square__size = size   
        
    
    def size(self):
        return self._Square__size

    def size(self, value):
        self._Square__size
        self._Square__size = size   
        if type(value) is not int:
            raise TypeError('size must be an integer')
            
        elif value < 0:
            raise ValueError('size must be >= 0')
            
        else:
            pass
        
      

    def area(self):
        return self._Square__size ** 2
