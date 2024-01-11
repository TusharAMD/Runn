# Battle City Game
## About the Game
Battle City is a very fun and addicting online game. You start off by either building a city or applying for a job in a city built by someone else. Your goal is to defend your city while attacking and destroying enemy cities. All of this is done in real-time from the comfort of your tank! The best thing about Battle City is that it has been released under the GPLv3 open source license. This license gives ownership of the game to the community and ensures Battle City will stay free and open source forever! 

## How does this work?
The game runs on a server with a game window and listens for two connections: player1 and player2. Each player is a separate client (tank) connected to the game server. The clients control their tanks by sending actions to the server. The game starts when both connections are established and greetings messages are send to both clients. The client's moves are defined once, and do not undergo any changes during the gameplay.

## What is the goal?
There are two goals:
- SURVIVE in 2 minutes
- Get more points than the second player

## How to achieve that?
In order to survive and score the biggest amount of points, you need to program the moves of your client with a thorough and clever approach.

## Scores:
- 1 for each destroyed tiny-brick
- 5 for each 'freeze' second player
- 200 for each destroyed NPC tank
- 100 for each coin

## Game Controls:
There are usually two players in this game.
- Player 1: * movement: up/left/down/right * fire: space
- Player 2: * movement: w/d/s/a * fire: f

## Libraries Used:
- numpy
- tensorflow
- imutils
- PyAutoGUI
- opencv_python
- pygame
- time
- random
- uuid
