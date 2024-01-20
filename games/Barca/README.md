# Barca Chess Variant

Barca is a chess variant where each player controls two mice (which move like chess rooks), lions (bishops), and elephants (queens). The objective of the game is to occupy three of the four "watering hole" spaces near the middle of the board.

## Game Rules

- Mice are afraid of lions, lions are afraid of elephants, and elephants are afraid of mice. Afraid animals are in "check" and must move away before other animals can move.
- The game is played on a 10x10 board.
- The four "watering hole" spaces are critical for victory; players aim to occupy three of these spaces.
- The available player pieces are Square Mouse (Mo), Square Lion (Li), Square Elephant (El), Round Mouse (Mo), Round Lion (Li), and Round Elephant (El).

## Constants

- `SQUARE_PLAYER` and `ROUND_PLAYER`: Constants representing the two players.
- `BOARD_WIDTH` and `BOARD_HEIGHT`: Dimensions of the game board.
- Various strings representing animal pieces and the board layout.

## Directions

- Constants representing different movement directions (UP, DOWN, LEFT, RIGHT, etc.).
- `ANIMAL_DIRECTIONS` and `FEARED_ANIMAL_DIRECTIONS`: Dictionaries defining valid move directions for each animal piece.

## Functions

- `main()`: Main game loop that initializes the game and handles player turns.
- `getNewBoard()`: Initializes and returns a new game board.
- `displayBoard(board)`: Displays the current state of the game board.
- `getAnimalStr(board, x, y)`: Returns a string representation of the animal at a given position, considering fear.
- `isOnBoard(x, y)`: Checks if a given position is within the board boundaries.
- `doPlayerMove(player, board)`: Handles player input for selecting and moving pieces.
- `movePiece(moveFrom, moveTo, board)`: Moves a piece from one position to another on the board.
- `getPieceMovements(player, board)`: Returns a list of valid moves for a given player.
- `xyToA1(x, y)`: Converts (x, y) coordinates to user-friendly coordinates (e.g., A1, B5).
- `A1ToXy(space)`: Converts user-friendly coordinates to (x, y) coordinates.
- `isWinner(player, board)`: Checks if a player has occupied three of the four watering holes.

## Running the Game

If the script is executed directly, the game will start, and players can take turns making moves until one of them wins or the game is quit.

To start the game, run the script in a Python environment:

```bash
python script_name.py
