# **Code Expansion**

An example of how we could extend our code is by adding an additional jump. Our current code allows the user to make only one jump at a time, and not consecutive jumps in one go. To allow this, we can expand the code as follows:
- The code will extend the move class:
   1. a while loop that checks if player can move
   2. the player moves
   3. checks if a piece is killed
   4. if true go back to step 2, false then it ends loops
   - pseudo code example:
     ```
     while(player_can_move):
           move
           if piece killed:
              player_can_move = True
           else:
              player_can_move = False
      end of loop
      ```
