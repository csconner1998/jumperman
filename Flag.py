import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Flag(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("flag.tga")        
        self.rect = self.image.get_rect()


