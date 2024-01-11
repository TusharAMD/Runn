# Dinosaur Game using Gesture Control
## Idea of the Game
What do we see on Chrome when there is no internet connection? The classic Chrome Dinosaur Game: T-Rex Runner Game (aka the No Internet Game)! Simply press the space bar and the dinosaur will start running. Press the arrow-up key to make the dinosaur jump; the longer you press the key, the higher it jumps. Every single one of us must’ve played this game at least once.
Has it ever crossed your mind that you can play this very game using just your palm?
Here, we can control Google Chrome Offline Dinosaur game using OpenCV. It processes the image and sends the signal to jump or not.

Here’s how we can play the Chrome-Dino game with just our palm. It is very much possible with a special Python module named PyAutoGUI.

## Stepwise procedure:
1. Open up the camera and draw a rectangle
2. Blur the image and convert it into HSV
3. Erode, Dilate and Threshold
4. Contour 
5. Run the code and play the game

# Features:
- Step 1: Real-time gesture Detection
- Step 2: Find the landmarks for the detected face
- Step 3: Build the Jump Control mechanism for the Dino
- Step 4: Build the Crouch Control mechanism
- Step 5: Perform Calibration
- Step 6: Keyboard Automation with PyautoGUI
- Step 7: Build the Final Application

## Libraries Used:
- numpy==1.15.2
- imutils==0.5.1
- PyAutoGUI==0.9.38
- opencv_python==3.4.3.18
- pygame==1.9.4
