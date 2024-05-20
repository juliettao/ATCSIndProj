# ATCSIndProj
ATCS final independent project
Connect 4

For my final project in this class, I decided to write a connect4 program. I was
inspired to pursue this project after attempting to write this program in java last
year in APCS, though last year Kate Lim and I sort of gave up on trying to get it to
work after failing to many times...

During this project, I attempted to create a connect4 game. I followed the
classic rules of the game, with a player winning by getting to 4 but only vertically or 
horizontally. I created the game to be one-player, with the player playing against the computer. 
With the computer, I had it only placing pieces around its own previous pieces to try to win.

Initially, I had a really complicated bunch of if statement to determine where the
computer will put its piece, but eventually I just had both the player and computer pick
a column to drop the piece in. I have a couple functions: print board, drop piece, computer 
move, player move, play game and checkWinner. I tried to to let the player win in all directions, 
but that ended up being to many checks and was really complicated, so eventually I whittled
down to just checking vertically and horizontally.

In summary, the main functions that the program performs are creating a board, allowing the
player to pick a spot to drop a piece, and allowing the computer to pick a column near
a previously placed piece. The rest of the program mainly checks if spaces on the 
board are available to place a piece and plays the game while checking for a winner.

Although I think the program is pretty successful in what I was trying to do, its biggest flaw 
is that the computer is only trying to win- but not prevent the player from winning. Because of 
this, it is really easy for the player to win basically every time. If I had better coding abilities,
I would probably try to code the computer to block the players moves to make the game a bit more 
realistic and challenging for the player. However, I went with this simpler version so that the 
game could function properly and be able to be played.


*Throughout the project, I referenced the website GeeksForGeeks a couple of times for basic
already-existing python functions in order to simplify my code in some spots of perform 
functions I didn't know how to write. The places where I referenced this outside material
are noted in the connect4 program.