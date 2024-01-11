# Mine Sweeper Game
## About the Game
Minesweeper rules are very simple. The board is divided into cells, with mines randomly distributed. To win, you need to open all the cells. The number on a cell shows the number of mines adjacent to it. Using this information, you can determine cells that are safe, and cells that contain mines. Cells suspected of being mines can be marked with a flag using the right mouse button.

## Input:
The input will consist of an arbitrary number of fields. The first line of each field contains two integers n and m ( 0 < n, m100) which stand for the number of lines and columns of the field, respectively. Each of the next n lines contains exactly m characters, representing the field.
Safe squares are denoted by ``.'' and mine squares by ``*,'' both without the quotes. The first field line where n = m = 0 represents the end of input and should not be processed.

## Output:
For each field, print the message Field #x: on a line alone, where x stands for the number of the field starting from 1. The next n lines should contain the field with the ``.'' characters replaced by the number of mines adjacent to that square. There must be an empty line between field outputs.

### Sample Input
- 4 4
*...
....
.*..
....
- 3 5
**...
.....
.*...
0 0

### Sample Output
- Field #1:
*100
2210
1*10
1110
- Field #2:
**100
33200
1*100
*/

## Libraries Used:
- numpy==1.15.2
- imutils==0.5.1
- PyAutoGUI==0.9.38
- opencv_python==3.4.3.18
- pygame==1.9.4

