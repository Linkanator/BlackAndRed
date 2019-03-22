class Board:
    '''A Board object that keeps track of which tiles are being occupied and by 
    which player each tile is being occupied by'''

    def __init__(self):
        """Initializes an 8x8 Board with 12 pieces for player1 and 12 for player2
        """
        self.board = []
        self.board.append(["p2", "o", "p2", "o", "p2", "o", "p2", "o"])
        self.board.append(["o", "p2", "o", "p2", "o", "p2", "o", "p2"])
        self.board.append(["p2", "o", "p2", "o", "p2", "o", "p2", "o"])
        self.board.append(["o", "o", "o", "o", "o", "o", "o", "o"])
        self.board.append(["o", "o", "o", "o", "o", "o", "o", "o"])
        self.board.append(["o", "p1", "o", "p1", "o", "p1", "o", "p1"])
        self.board.append(["p1", "o", "p1", "o", "p1", "o", "p1", "o"])
        self.board.append(["o", "p1", "o", "p1", "o", "p1", "o", "p1"])

    def is_tile_empty(self, x, y):
        """Returns if the tile at the specified location is empty or occupied by 
        a player
        @param x horizontal index of the tile
        @param y vertical index of the tile
        @return a string indicating either an empty space or a space occupied by
        player1 or player2
        """
        return self.board[x][y]

    def empty_tile(self, x, y):
        """Empties the specified tile
        @param x horizontal index of the tile
        @param y vertical index of the tile
        """
        self.board[x][y] = "o"

    def fill_tile(self, x, y, player):
        """Occupy the spicified tile with the provided player
        @param x horizontal index of the tile
        @param y vertical index of the tile
        @param player a string indicating if player1 or player2 are occupying
        the tile
        """
        if((y == 0 and player == "p1") or player == "p1c"):
            self.board[y][y] = "p1c"
        elif((y == 7 and player == "p2") or player == "p2c"):
            self.board[y][x] = "p2c"
        else:
            self.board[y][x] = player

        
    def clear_board(self):
        """Clear the game board
        """        
        for x in range(8):
            for y in range(8):
                self.board[x][y] = "o"
