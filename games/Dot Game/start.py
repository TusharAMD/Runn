import math
import pygame

SCREEN = WIDTH, HEIGHT = 300, 300
CELLSIZE = 40
PADDING = 20
ROWS = COLS = (WIDTH - 4 * PADDING) // CELLSIZE
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)

WHITE = (255, 255, 255)
RED = (252, 91, 122)
BLUE = (78, 193, 246)
GREEN = (0, 255, 0)
BLACK = (12, 12, 12)

font = pygame.font.SysFont('cursive', 25)