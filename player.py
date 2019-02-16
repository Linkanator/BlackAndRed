class Player:
    '''A Player object that stores the pieces each player owns and provides methods to 
    manipulate the pieces.
    '''

    """Initializes a Player
    @param pieces: a list of checker pieces that the player starts off with
    """
    def __init__(self, pieces):
        self.pieces = pieces

    def add_piece(self, piece):
        self.pieces.append(piece)

    def kill_piece(self, piece):
        self.pieces.remove(piece)

    def get_pieces(self):
        return self.pieces
