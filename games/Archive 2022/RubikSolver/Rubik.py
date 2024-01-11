# Rubik Cube Solver Using Python



from Cube.cube import Cube
from Cube.Solver import kociemba
from Cube.Solver import beginners
import time
import math


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


cubestrings = []
sides = ['white', 'orange', 'green', 'red', 'blue', 'yellow']
for i in range(6):
    cubestrings.append(input(f'type in side {sides[i]}: '))
    if len(cubestrings[i]) == 9:
        pass
    else:
        print('you fucking idiot you bitch fuck you wrote it ALL WRONG')

cube = Cube(''.join(cubestrings))
print(cube)
start = time.time()
solution = beginners.solve(cube)
cube.sequence(solution)
end = time.time()
print('Done!')
print(f'solution: {solution}')
print(cube)
time = end - start
print(f"time: {round_half_up(time, 3)} seconds.")

input()