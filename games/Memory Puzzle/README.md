# Memory Puzzle Game
## About the Game
In the Memory Puzzle game, several icons are covered up by white boxes. There are two of each icon. The player can click on two boxes to see what icon is behind them. If the icons match, then those boxes remain uncovered. The player wins when all the boxes on the board are uncovered. To give the player a hint, the boxes are quickly uncovered once at the beginning of the game.

## How to play
1. Click on the tiles will display the hidden icon
2. You have to match two tiles of the same type at a time
3. Try to match all pairs in as minimum moves as possible
4. Ratings calculated based on number moves
5. if total moves <= 20, then rating is 3 stars
6. If total moves in between 21 and 29, then rating is 2 stars
7. If total moves >=30, then rating is 1 star

## Game Features:
1. Match Cards are locked and display with light green color
2. Unmatched cards are little shakes with red color and disappear the with black screen
3. Count moves based on each pair card selected
4. When start the game the timer will start
5. Display ratings based on number of moves
6. Display dialog model with scores, moves and ratings when you win the Game

## Libraries Used:
- numpy==1.15.2
- imutils==0.5.1
- PyAutoGUI==0.9.38
- opencv_python==3.4.3.18
- pygame==1.9.4

