import pygame

class PickUps(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
        width = 40
        height = 40
        self.images = []
        self.image_rotate = pygame.image.load("PickUps.tga")
        for x in range(180):
            self.images.append(pygame.transform.rotate(self.image_rotate, 2*x))
        self.index = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (width, height)) 
        self.rect = self.image.get_rect()

        player = None

        score = None

        

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            PickUps.kill(self)
            

            
            
            
            

        
        
