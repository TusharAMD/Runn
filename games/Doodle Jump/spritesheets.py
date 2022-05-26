import pygame
from settings import *
vec=pygame.math.Vector2

class SpriteSheet:
    def __init__(self):
        self.spritesheet=pygame.image.load(spritesheet_file_name).convert()

    def imageLoad(self,x,y,width,height):
        image=pygame.Surface((width,height))
        image.blit(self.spritesheet,(0,0),(x,y,width,height))
        image=pygame.transform.scale(image,(width//3,height//3))#remove this
        return image