''' class of square
    creates private size
'''
class Square():
    ''' instantiate size
    private attribute: size
    '''
    def __init__(self, size= 0):
        self._Square__size = size 
        

    def __dict__(self, size):
        self._Square__size = size 
        if type(self.size) is not int:
            raise TypeError('size must be an integer')
        elif self.size < 0:
            raise ValueError('size must be >= 0')
            
