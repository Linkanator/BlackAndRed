import pygame

class CheckersModel:
    def __init__():
        """Initializes the game. Keep tracks of players, board and if game is over"""
        self.player1 = Player()
        self.player2 = Player()
        self.board = Board()
        self.curr_player = player1
        self.game_over = False

    def move(piece, move_from, move_to):
        """Checks if move is valid and changes board accordingly
        @return 0 is move is successful, 1 if move is invalid
        """
        if (self.curr_player == self.player1):
            player = "p1"
            crown = "p1c"
            next_player = "p2"
            next_crown = "p2c"            
        else:
            player = "p2"
            crown = "p2c"
            next_player = "p1"
            next_crown = "p1c"            
            
        "Moves a piece from one tile to another, and saves the move in self.move"
        to_tile = self.board.is_tile_empty(move_to.x, move_to.y)
        from_tile = self.board.it_tile_empty(move_from.x, move_from.y)
        
        #check if correct piece is being moved to an empty tile
        if(to_tile != "o"):
            return 1
        elif(from_tile == "o"):
            return 1
        elif(from_tile != player or from_tile != crown):
            return 1 
            
        #check if piece is moving in correct direction    
        if(self.curr_player == "p1"):
            if(move_from.y - move_to.y < 0 and from_tile != "p1c"):
                return 1
        if(self.curr_player == "p2"):
            if(move_from.y - move_to.y > 0 and from_tile != "p2c"):
                return 1

        #check if piece is making a valid non-jump move
        if(move_from.x - move_to.x == 1 or move_from.x - move_to.x == -1):
            if(move_from.y - move_to.x == 1 or move_from.y - move_to.x == -1):
                self.board.empty_tile(move_from.x, move_from.y)
                self.board.fill_tile(move_to.x, move_to.y, from_tile)
                return 0
        #check if piece is jumping up and right
        elif(move_from.x - move_to.x == 2 and move_from.y - move_from.y == 2):
            if(self.board.is_tile_empty(move_from.x + 1, move_from.y + 1) == next_player \
                or self.board.is_tile_empty(move_from.x + 1, move_from.y + 1) == next_crown):
                self.board.empty_tile(move_from.x, move_from.y)
                self.board.fill_tile(move_to.x, move_to.y, from_tile)
                return 0
            else:
                return 1
        #check if piece is jumping up and left
        elif(move_from.x - move_to.x == -2 and move_from.y - move_from.y == 2):
            if(self.board.is_tile_empty(move_from.x - 1, move_from.y + 1) == next_player \
                or self.board.is_tile_empty(move_from.x - 1, move_from.y + 1) == next_crown):
                self.board.empty_tile(move_from.x, move_from.y)
                self.board.fill_tile(move_to.x, move_to.y, from_tile)
                return 0
            else:
                return 1   
        #check if piece is jumping down and right
        elif(move_from.x - move_to.x == 2 and move_from.y - move_from.y == -2):
            if(self.board.is_tile_empty(move_from.x + 1, move_from.y - 1) == next_player \
                or self.board.is_tile_empty(move_from.x + 1, move_from.y - 1) == next_crown):
                self.board.empty_tile(move_from.x, move_from.y)
                self.board.fill_tile(move_to.x, move_to.y, from_tile)
                return 0
            else:
                return 1      
        #check if piece is jumping down and left
        elif(move_from.x - move_to.x == -2 and move_from.y - move_from.y == -2):
            if(self.board.is_tile_empty(move_from.x - 1, move_from.y - 1) == next_player \
                or self.board.is_tile_empty(move_from.x - 1, move_from.y - 1) == next_crown):
                self.board.empty_tile(move_from.x, move_from.y)
                self.board.fill_tile(move_to.x, move_to.y, from_tile)
                return 0
            else:
                return 1 
        return 1
        
        
    def player_turn(self):
        "Changes the turn of the curr_player"
        if self.curr_player == self.player1:
            self.curr_player = self.player2
        else:
            self.curr_player  = self.player1

    def is_game_won(self):
        "Checks if any player has won, returns True if true, and False otherwise"
        "Checks if any player has won, returns True if true, and False otherwise"
        if(player1.get_pieces() == 0):
            return True, "player1"
        elif(player2.get_pieces() == 0):
            return True, "player2"
        else:
            return False, "none"

