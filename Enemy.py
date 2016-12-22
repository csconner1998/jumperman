import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Enemy(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
        self.images = []
        width = 60
        height = 60
        for x in range(15):
            self.images.append(pygame.image.load("enemy01.tga"))
        for x in range(15):
            self.images.append(pygame.image.load("enemy02.tga"))
        for x in range(15):
            self.images.append(pygame.image.load("enemy03.tga"))
        for x in range(15):
            self.images.append(pygame.image.load("enemy02.tga"))
        self.index = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (width, height))
        
        self.rect = self.image.get_rect()
        player = None
 
        level = None

        BulletList = None

    def update(self):
        self.index = 20
        self.image = self.images[self.index]

        for bullet in self.BulletList:
            hit1 = pygame.sprite.collide_rect(self, bullet)
            if hit1:
                Enemy.kill(self)
                bullet.kill()

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            pygame.time.wait(500)
            pygame.quit()
            sys.exit()
        
