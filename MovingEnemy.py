import pygame, sys
from Enemy import Enemy
class MovingEnemy(Enemy):
    change_x = 0
    change_y = 0
 
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
 
    player = None
 
    level = None

    BulletList = None
 
    def update(self):

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            pygame.time.wait(500)
            pygame.quit()
            sys.exit()
                
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we the player
        for bullet in self.BulletList:
            hit1 = pygame.sprite.collide_rect(self, bullet)
            if hit1:
                Enemy.kill(self)
                bullet.kill()
 
        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
