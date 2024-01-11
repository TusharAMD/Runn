
import random

class Card:
    """Individual card object."""
    instances = []
    guesses = []
    correct = []

    def __init__(self, x, y, icons):
        self.x = x
        self.y = y
        self.mode = 2
        self.icon = icons[0][0]
        self.color = icons[0][1]
        self.rect = (0, 0, [0, 0, 0, 0])
        Card.instances.append(self)