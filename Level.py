import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Level():
 
    def __init__(self, player, backround, BulletList):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.pickup_list = pygame.sprite.Group()
        self.gate_list = pygame.sprite.Group()
        self.flag_list = pygame.sprite.Group()
        self.win_list = pygame.sprite.Group()
        self.player = player
        self.backround = backround
 
        # How far this world has been scrolled left/right
        self.world_shift = 0
 
    # Update stuff on this level
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        self.pickup_list.update()
        self.gate_list.update()
        self.flag_list.update()
        self.win_list.update()
        if len(self.pickup_list) == 0:
            for gates in self.gate_list:
                gates.kill()


 
    def draw(self, screen):
 
        # Draw the background
        backrounds = pygame.image.load(self.backround).convert()
        screen.blit(backrounds, (0,0))
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.pickup_list.draw(screen)
        self.gate_list.draw(screen)
        self.win_list.draw(screen)
        if (len(self.pickup_list) == 0) and (len(self.enemy_list)==0):
            self.flag_list.draw(screen)
 
    def shift_world(self, shift_x):
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for pikup in self.pickup_list:
            pikup.rect.x += shift_x

        for gate in self.gate_list:
            gate.rect.x += shift_x

        for flag in self.flag_list:
            flag.rect.x += shift_x
 
 
