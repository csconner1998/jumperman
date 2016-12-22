import pygame, sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Gate(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Gate.tga")
        self.image = pygame.transform.scale(self.image, (180, 600))
        
        self.rect = self.image.get_rect()

    def update(self):
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            pygame.time.wait(500)
            pygame.quit()
            sys.exit()
