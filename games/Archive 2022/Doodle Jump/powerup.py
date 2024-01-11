import pygame
from settings import *
from spritesheets import *

class PowerUps(pygame.sprite.Sprite):
    def __init__(self,platform,game):
        self.groups=game.powerups
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.plat=platform
        self.spritesheetsobj = SpriteSheet()
        self.image = self.spritesheetsobj.imageLoad(563,1843,133,160)
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.scale(self.image, (133//6,160//6))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 5
        print "Power-UP ADDED!"


    def update(self):
        self.rect.bottom=self.plat.rect.top - 5
        if not self.game.platforms.has(self.plat):
            self.kill()

