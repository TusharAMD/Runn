import pygame
from settings import *
import random

class lowPlatform(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((w,h))
        color=platform_colors[random.randrange(0,len(platform_colors))]
        self.image.fill(green)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y