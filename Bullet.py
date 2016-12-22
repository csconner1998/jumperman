import pygame, sys
from pygame.locals import *
from math import *


class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        width = 16
        height = 9

        self.image = pygame.image.load("Fireball.tga")
        self.image = pygame.transform.scale(self.image, (width, height)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += 4
