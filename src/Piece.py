import sys, pygame, random
import os

class Piece:
    '''
    A Box Actor.
    '''

    def __init__(self, icon_file, stage, x=0, y=0):
        '''
        (Actor, str, Stage, int, int) -> None
        Construct a Box on the given stage, at given position.
        '''

        super().__init__(icon_file, stage, x, y)

    def move(self, other, dx, dy):
        '''
        (Actor, Actor, int, int) -> bool
        Move this Actor by dx and dy, if possible. other is the Actor that asked to make this move.
        If a move is possible (a space is available) then move to it and return True.
        If another Actor is occupying that space, ask that Actor to move to make space, and then
        move to that spot, if possible.
        If a move is not possible, then return False.
        '''

        new_x = self._x + dx
        new_y = self._y + dy

        if self._stage.is_in_bounds(new_x, new_y):
            if not self._stage.get_actor(new_x, new_y):
                super().move(other, dx, dy)
                return True
            elif isinstance(self._stage.get_actor(new_x, new_y), Box):
                if self._stage.get_actor(new_x, new_y).move(self, dx, dy):
                    super().move(other, dx, dy)
                    return True
            elif isinstance(self._stage.get_actor(new_x, new_y), StickyBox):
                if self._stage.get_actor(new_x, new_y).move(self, dx, dy):
                    super().move(other, dx, dy)
                    return True
        return False