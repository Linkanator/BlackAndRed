import pygame

class Checkers:
    """Class that begins the game and updates the view."""
    self.controller: CheckersController
    self.model: CheckersModel

    def __init__(self) -> None:
        """Initialize a new Checkers object."""
        self.model = CheckersModel()
        self.controller = CheckersController(self.model)

    def update(self) -> None:
        """Runs game for one round and updates view based on changes in the game."""
        while not self.model.is_game_won():
            self.controller.play()
            self.model.move()
            inner = self.controller.winning_player()
        winner = self.controller.winning_player()
        print(f"Congratulations on your win, Player {winner}!")


class CheckersController:
    def __init__(self, model: CheckersModel) -> None:
        self.model = model

    def play(self):
        is_won, loser = self.model.is_game_won()
        while not is_won:
            move_is_valid = False
            while not move_is_valid:
                move_from = input("Choose the location of the piece to move")
                move_to = input("Choose the location to move the piece to")
                returned_value = self.model.move(move_from, move_to)
                if not returned_value:
                    move_is_valid = True
            is_won, loser = self.model.is_game_won()
            if loser == "player1":
                print("Congratulations on your win, Player 2!")
            else:
                print("Congratulations on your win, Player 1!")

    def winning_player(self):


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
        @param move_from   a PlayerMove object that indicates which tile the player is moving from
        @param move_to     a PlayerMove object that indicates which tile the player is moving to
        @return 0          move is successful
        @return 1          move is invalid
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
        
        #saves the piece at the from and to tile, if there is one    
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
        '''Changes curr_player to the next turn's player'''
        if self.curr_player == self.player1:
            self.curr_player = self.player2
        else:
            self.curr_player  = self.player1

    def is_game_won(self):
        '''Checks if any player has won.
        @return True, player    game has been won, player that lost
        @return False, player   game has not been won, no player
        '''
        if(player1.get_pieces() == 0):
            return True, "player1"
        elif(player2.get_pieces() == 0):
            return True, "player2"
        else:
            return False, "none"

