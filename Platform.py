import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Platform(pygame.sprite.Sprite):
 
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load("Platform.tga")
        self.image = pygame.transform.scale(self.image, (width, height))
        
        self.rect = self.image.get_rect()
