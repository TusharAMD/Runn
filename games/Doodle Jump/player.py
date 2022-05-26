import pygame
from settings import *
vec=pygame.math.Vector2
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_pikachu_sprite=pygame.sprite.Sprite()
        self.img_pikachu_sprite.image = pygame.image.load('pikachu.png').convert()
        self.img_pikachu_sprite.rect=self.img_pikachu_sprite.image.get_rect()
        self.pos = vec(display_width / 2, display_height - 100)
        self.img_pikachu_sprite.rect.topleft =[self.pos.x,self.pos.y]
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.mask_image = pygame.mask.from_surface(self.img_pikachu_sprite.image)
        return img_pikachu_sprite

