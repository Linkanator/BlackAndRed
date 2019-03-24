class Player:
    '''A Player object that keeps track of the number of pieces each player owns
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
    
