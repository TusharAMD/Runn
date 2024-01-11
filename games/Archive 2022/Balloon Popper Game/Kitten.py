import pygame
from Balloon import Balloon

class Kitten(Balloon):

    def __init__(self, screen, settings):

        Balloon.__init__(self, screen, settings)
        self.image = pygame.image.load('kitten_50px.png').convert_alpha()
