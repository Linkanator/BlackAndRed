class Player:
    '''A Player object that stores the pieces each player owns and provides methods to 
    manipulate the pieces.
    '''

    def __init__(self):
        """Initializes a Player with 12 game pieces
        """        
        self.num_pieces = 12

    def kill_piece(self):
        """Removes a checker piece from player
        """        
        self.num_pieces -= 1
        
    def get_pieces(self):
        """Returns the number of pieces player still has
        """
        return self.num_pieces
    
