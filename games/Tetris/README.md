# Tetris Gesture Control Game
## About the Game
Tetris is the addictive puzzle game that started it all, embracing our universal desire to create order out of chaos. The Tetris game was created by Alexey Pajitnov in 1984—the product of Alexey’s computer programming experience and his love of puzzles. In the decades to follow, Tetris became one of the most successful and recognizable video games, appearing on nearly every gaming platform available. 
Class Piece represents a game piece ("tetrimino"), it defines how a piece rotates and kicks off obstacles.

Class Board represents the geometric state of the board. It stores which tiles are occupied, the position of the current piece and processes required motions obeying geometric constraints. Class Tetris operates on Board and defines game timings, user input processing and scoring.

The drawing functions are implemented in render. It defines several convenience classes to render board, pieces and text using simple OpenGL shaders.

File utility contains classes representing a shader, a texture and a font glyph. As well as functions to load a texture and a font from a file.
The game initialization and main loop is implemented in game.cpp in the most straightforward manner without farther abstractions.


## Game Controls:
The following list contains used control keys:
- Arrows - used for the moving of a tetris block
- Space - rotates the tetris block
- q - quit the game
- p - pause the game

## Features:
- Left/right arrows to move the piece laterally
- Up arrow to make it pivot
- Down arrow to accelerate it (maintain key)
- Space bar for hrd drop
- Esc to pause the game

## Libraries Used:
- numpy==1.15.2
- imutils==0.5.1
- PyAutoGUI==0.9.38
- opencv_python==3.4.3.18
- pygame==1.9.4
