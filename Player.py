import pygame, sys

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
TRANSP = (0, 0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, image1, image2, image3):
        
        # Call the parent's constructor
        super().__init__()
         
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 60
        height = 60
        self.images = []
        for x in range(20):
            self.images.append(pygame.image.load(image1))
        for x in range(20):
            self.images.append(pygame.image.load(image2))
        for x in range(20):
            self.images.append(pygame.image.load(image3))
        for x in range(20):
            self.images.append(pygame.image.load(image2))
        self.index = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (width, height))   
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None
 
    def update(self):
        # Gravity
        self.calc_grav()

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            pygame.quit()
            sys.exit()
 
    def jump(self):
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
 
    # Player-controlled movement:
    def go_left(self):
        self.change_x = -6
 
    def go_right(self):
        self.change_x = 6
 
    def stop(self):

        self.change_x = 0
 
 
