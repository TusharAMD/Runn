# Rotating Cube

A rotating cube animation by Abhinesh Jha.

## How to Run

- Run the script in a Python environment.
- Press `Ctrl-C` to stop the rotating cube animation.

## Constants

- `PAUSE_AMOUNT`: Pause length in seconds.
- `WIDTH` and `HEIGHT`: Dimensions of the display window.
- `SCALEX` and `SCALEY`: Scaling factors for adjusting the 3D points to 2D.
- `TRANSLATEX` and `TRANSLATEY`: Translation factors for moving the 2D points.
- `LINE_CHAR`: Character used for displaying points on the screen.
- `X_ROTATE_SPEED`, `Y_ROTATE_SPEED`, and `Z_ROTATE_SPEED`: Rotation speeds along different axes.

## Functions

- `line(x1, y1, x2, y2)`: Returns a list of points in a line between the given points.
- `rotatePoint(x, y, z, ax, ay, az)`: Returns an (x, y, z) tuple of the rotated coordinates.
- `adjustPoint(point)`: Adjusts the 3D XYZ point to a 2D XY point fit for displaying on the screen.

## Cube Corners

- `CUBE_CORNERS`: Stores the XYZ coordinates of the corners of a cube.

## Main Program Loop

The script continuously rotates the cube along different axes and displays it on the screen.

Enjoy the rotating cube animation!

**Note:** Try adjusting the rotation speeds and the `LINE_CHAR` variable to experiment with different visual effects.
