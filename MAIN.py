import pygame, sys
from Player import Player
from Platform import Platform
from Level import Level
from Level_01 import Level_01
from Level_02 import Level_02
from Level_03 import Level_03
from Level_04 import Level_04
from Level_Win import Level_Win
from Bullet import Bullets
from Gate import Gate
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# Screen dimensions
SCREEN_WIDTH = 1530
SCREEN_HEIGHT = 600


# Import Backround
Backround1 = "BG01.tga"
Backround2 = "BG02.tga"
Backround3 = "BG03.tga"

player_image1 = "sprite01.tga"
player_image2 = "sprite02.tga"
player_image3 = "sprite03.tga"




 
def main():
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

 
    pygame.display.set_caption("JumperMan")
    
    
    # Create the player
    player = Player(player_image1, player_image2, player_image3)

    # Load and play music
    pygame.mixer.music.load("Fly_High.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.3)

    bang = pygame.mixer.Sound("Laser.wav")
    
    # Make a list of bullets
    BulletList = pygame.sprite.Group()

    # Create all the levels
    level_list = []
    level_list.append(Level_01(player, Backround1, BulletList))
    level_list.append(Level_02(player, Backround2, BulletList))
    level_list.append(Level_04(player, Backround3, BulletList))
    level_list.append(Level_03(player, Backround2, BulletList))
    level_list.append(Level_Win(player, Backround1, BulletList))


 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 100
    player.rect.y = SCREEN_HEIGHT - player.rect.height - 100
    active_sprite_list.add(player)
 



    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()



    # -------- Main Program Loop -----------
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                    
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_SPACE:
                    bang.play()
                    bullet = Bullets(player.rect.right-20,player.rect.bottom - 27)
                    BulletList.add(bullet)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_SPACE:
                    pass
 
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()

        # Update the Bullets
        BulletList.update()

        
        # Remove bullet when it gets off screen
        for bullet in BulletList:
            if bullet.rect.x >= SCREEN_WIDTH:
                BulletList.remove(bullet)
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
 
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            player.rect.y = SCREEN_HEIGHT - player.rect.height - 100
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
                BulletList.empty()
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        BulletList.draw(screen)
         
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    pygame.quit()
 
if __name__ == "__main__":
    main()
