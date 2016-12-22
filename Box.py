import pygame

GREY = (100, 100, 100)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Box(pygame.sprite.Sprite):
 
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(GREY)
        
        self.rect = self.image.get_rect()
