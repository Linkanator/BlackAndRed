## Code Structure

### Descriptions of classes and their functions can be found below.

```src/ck.py``` contains the CheckersModel class. It holds all code for keeping track of player turns, checking if moves are valid and adjusting the board accordingly, as well as code for checking if the game has been won.

```src/game_board.py``` contains the Board class that keep tracks of where each player has their pieces by filling and emptying tiles according to the players' moves.

```src/moves.py```  contains the Move class that converts user input into an array with x and y values from 1-8.

```scr/ckgame.py``` contains code for drawing the Checker board on the GUI.

```scr/player.py``` contains the Player class that keeps track of the number of pieces each player still has on the board.
