import pygame
import sys
from math import *

pygame.init()
width = 660
height = 360
outerHeight = 400
margin = 30
display = pygame.display.set_mode((width, outerHeight))
pygame.display.set_caption("Ball Pool")
clock = pygame.time.Clock()
