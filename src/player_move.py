class PlayerMove:
    '''Initializes a Move object that stores the x and y coordinates on the board.
    '''
    
    def __init__(self, x, y):
        """Sets the x and y coordinates on the board
        """
        self.x = x
        self.y = y
        
    def x(self):
        return self.x
    
    def y(self):
        return self.y
