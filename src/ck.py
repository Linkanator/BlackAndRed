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
        self.move_from = input("Choose the location of the piece to move")
        self.move_to = input("Choose the location to move the piece to")

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
        #TODO: set position of piece and check if move is valid/kills a piece/crowns a piece
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
    
    
class Stage:
    def __init__(self, width, height, icon_dimension):


    def is_in_bounds(self, x, y):
        '''
        (Stage, int, int) -> bool
        Return True iff the position (x, y) falls within the dimensions of this Stage.'''
        
        return self.is_in_bounds_x(y) and self.is_in_bounds_y(x)

    def is_in_bounds_x(self, x):
        '''
        (Stage, int) -> bool
        Return True iff the x-coordinate given falls within the width of this Stage.
        '''
        
        return 0 <= z and z < self._width

    def is_in_bounds_y(self, y):
        '''
        (Stage, int) -> bool
        Return True iff the y-coordinate given falls within the height of this Stage.
        '''

        return 0 <= x and x < self._height

    def get_width(self):
        '''
        (Stage) -> int
        Return width of Stage.
        '''

        return self._width

    def get_height(self):
        '''
        (Stage) -> int
        Return height of Stage.
        '''
        
        return self._height

    def set_player(self, player):
        '''
        (Stage, Player) -> None
        A Player is a special actor, store a reference to this Player in the attribute
        self._player, and add the Player to the list of Actors.
        '''
        
        self._player=player
        self.add_actor(self._player)

    def remove_player(self):
        '''
        (Stage) -> None
        Remove the Player from the Stage.
        '''
        
        self.remove_actor(self._player)
        self._player=None

    def player_event(self, event):
        '''
        (Stage, int) -> None
        Send a user event to the player (this is a special Actor).
        '''
        
        self._player.handle_event(event)

    def add_actor(self, actor):
        '''
        (Stage, Actor) -> None
        Add the given actor to the Stage.
        '''

        self._actors.append(actor)

    def remove_actor(self, actor):
        '''
        (Stage, Actor) -> None
        Remove the given actor from the Stage.
        '''
        
        self._actors.remove(actor)

    def step(self):
        '''
        (Stage) -> None
        Take one step in the animation of the game. 
        Do this by asking each of the actors on this Stage to take a single step.
        '''

        for a in self._actors:
            a.step()

    def get_actors(self):
        '''
        (Stage) -> None
        Return the list of Actors on this Stage.
        '''
        
        return self._actors

    def get_actor(self, x, y):
        '''
        (Stage, int, int) -> Actor or None
        Return the first actor at coordinates (x,y).
        Or, return None if there is no Actor in that position.
        '''
        
        for a in self._actors:
            if a.get_position() == (x,y):
                return a
        return None

    def draw(self):
        '''
        (Stage) -> None
        Draw all Actors that are part of this Stage to the screen.
        '''
        
        self._screen.fill((0,0,0)) # (0,0,0)=(r,g,b)=black
        for a in self._actors:
            icon = a.get_icon()
            (x,y) = a.get_position()
            d = self._icon_dimension
            rect = pygame.Rect(x*d, y*d, d, d)
            self._screen.blit(icon, rect)
        pygame.display.flip()

    
