import pygame
from settings import *
from spritesheets import *
from random import choice,randrange
from powerup import *
#from main import *

class Cloud(pygame.sprite.Sprite):
    def __init__(self,game):
        self._layer=cloud_layer
        self.groups = game.all_sprites,game.clouds
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = choice(self.game.cloud_images)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        scale=randrange(50,101)/100
        self.image=pygame.transform.scale(self.image,(int(self.rect.width*scale), int(self.rect.height*scale)))
        self.rect.x = randrange(display_width - self.rect.width)
        self.rect.y = randrange(-500,-50)
        print "Cloud added"

    def update(self):
        if self.rect.top > display_height*2:
            self.kill()

