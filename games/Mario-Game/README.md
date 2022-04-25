# Mario Gesture Control Game Ideation
This is a simple python based game without touching the keyboard. This project is an application of hand detection model in Tensorflow. With the code, you could play many games on PC without using any keyboard. One of such games is the Mario Gesture-controlled game.

## About the Game
The game character's (Super Mario's) velocity depends on the speed and direction someone's fist or palm(hand) (as per user's choice) movements by using the computer's front-facing web camera. The 'stage' is just a 2D platform, with random holes on the ground and random clouds on sky. There is a timer upon game start, and that timer stops when the character collide to one of those holes or clouds (game end). A button resets the game stage.

The screen is splitted into 3 equal parts horizontally. There is mapping between your gesture and Mario's movement.

## Features:
- Open hand within the left part -> Left jump
- Closed hand within the left part -> Left run
- Open hand within the middle part -> Jump
- Closed hand within the middle part -> Do nothing
- Open hand within the right part -> Right jump
- Closed hand within the right part -> Right run

## Benefits:
The main aim of this proof-of concept game is that incentivizing the users to move/sport for keeping them healthy while they are having fun by playing a human - computer interaction game.

Games for human health, wellbeing, and fitness have recently begun to focus on making sports, physiological exercise, health, and wellbeing applications more playful, especially in light of the recent increase in sensor use and the quantified self movement.

## Libraries Used:
- numpy==1.15.2
- imutils==0.5.1
- PyAutoGUI==0.9.38
- opencv_python==3.4.3.18
- pygame==1.9.4
- tensorflow
