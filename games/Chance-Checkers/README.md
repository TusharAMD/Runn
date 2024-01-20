# Chance Checkers

A simple implementation of the game "Chance Checkers" by Abhinesh Jha.

## How to Play

- The game is played on an 8x8 checkerboard.
- Players are represented by 'X' and 'O'.
- The goal is to move your checkers to the opponent's side or capture all of the opponent's checkers.

## Constants

- `ALL_COLUMNS`: Represents all columns on the checkerboard.
- `ODD_CHECKER_COLUMNS` and `EVEN_CHECKER_COLUMNS`: Columns where odd and even rows can have checkers, respectively.
- `EMPTY`: The character used for an empty space on the board.

## Functions

- `main()`: Main game loop where players take turns making moves until one of them wins or the game is quit.
- `getNewBoard()`: Initializes a new checkerboard with empty spaces and starting pieces for players 'X' and 'O'.
- `displayBoard(board)`: Displays the current state of the checkerboard.
- `prevCol(column)` and `nextCol(column)`: Return the column letter that comes before and after a given column.
- `otherCheckers(checker)`: Returns a string of the opponent's checkers.
- `getPossibleDstMoves(board, srcSpace)`: Gets all possible destination moves from a given source space.
- `askForPlayerMove(board, player, moves)`: Asks the player to select a move.
- `makeMove(board, srcMove, dstMove)`: Carries out the move and returns a new checkerboard.
- `hasLost(board, player)`: Returns True if the player has no checkers left, otherwise False.

## Running the Game

If the script is executed directly, the game will start, and players can take turns making moves until one of them wins or the game is quit.

To start the game, run the script in a Python environment:

```bash
python script_name.py
