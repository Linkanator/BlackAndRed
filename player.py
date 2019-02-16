class Player:
    '''A Player object that stores the pieces each player owns and provides methods to 
    manipulate the pieces.
    '''

    """Initializes a Player
    @param Piece pieces: a list of checker pieces that the player starts off with
    """
    def __init__(self, pieces):
        self.pieces = pieces

    """Adds a checker piece to the current list of owned pieces
    @param Piece piece: checker piece to be added
    """
    def add_piece(self, piece):
        self.pieces.append(piece)

    """Removes a checker piece from the list of owned pieces
    @param Piece piece: checker piece to be removed
    """
    def kill_piece(self, piece):
        self.pieces.remove(piece)

    """Return list of checker pieces currently owned
    @return Array pieces: list of pieces
    """
    def get_pieces(self):
        return self.pieces
