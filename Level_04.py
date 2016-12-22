import pygame
from Level import Level
from Platform import Platform
from Enemy import Enemy
from MovingPlatform import MovingPlatform
from MovingEnemy import MovingEnemy
from PickUps import PickUps
from Gate import Gate
from Flag import Flag
from Win import Win

class Level_04(Level):
 
    def __init__(self, player, backround, BulletList):
 
        # Call the parent constructor
        Level.__init__(self, player, backround, BulletList)
 
        self.level_limit = -2000

        # Array with width, height, x, and y of platform
        level = [[210, 30, 100, 570],
                 [210, 50, 450, 500],
                 ]
        # Array with x and y of
        pickups = [[ 900, 340],
                   [ 600, 10],
                   [ 2500, 460]]
        
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for pikup in pickups:
            coin = PickUps()
            coin.rect.x = pikup[0]
            coin.rect.y = pikup[1]
            coin.player = self.player
            self.pickup_list.add(coin)
        

        flag = Flag()
        flag.rect.x = 2900
        flag.rect.y = 540
        self.flag_list.add(flag)
    

        gate1 = Gate()
        gate1.rect.x = 2840
        gate1.rect.y = 0
        gate1.player = self.player
        self.gate_list.add(gate1)

        block1 = MovingPlatform(200, 30)
        block1.rect.x = 800
        block1.rect.y = 520
        block1.boundary_left = 750
        block1.boundary_right = 1250
        block1.change_x = 4
        block1.player = self.player
        block1.level = self
        self.platform_list.add(block1)

        block2 = MovingPlatform(200, 30)
        block2.rect.x = 1250
        block2.rect.y = 100
        block2.boundary_left = 750
        block2.boundary_right = 1250
        block2.change_x = 2
        block2.player = self.player
        block2.level = self
        self.platform_list.add(block2)

        block3 = MovingPlatform(200, 30)
        block3.rect.x = 1550
        block3.rect.y = 50
        block3.boundary_top = 50
        block3.boundary_bottom = 550
        block3.change_y = 2
        block3.player = self.player
        block3.level = self
        self.platform_list.add(block3)

        block4 = MovingPlatform(200, 30)
        block4.rect.x = 2000
        block4.rect.y = 520
        block4.boundary_left = 1850
        block4.boundary_right = 2700
        block4.change_x = 2
        block4.player = self.player
        block4.level = self
        self.platform_list.add(block4)
        
        Badguy1 = MovingEnemy()
        Badguy1.rect.x = 1600
        Badguy1.rect.y = -10
        Badguy1.boundary_left = 1550
        Badguy1.boundary_right = 1690
        Badguy1.boundary_top = -10
        Badguy1.boundary_bottom = 520
        Badguy1.change_x = 2
        Badguy1.change_y = 2
        Badguy1.player = self.player
        Badguy1.level = self
        Badguy1.BulletList = BulletList
        self.enemy_list.add(Badguy1)

        Badguy2 = MovingEnemy()
        Badguy2.rect.x = 500
        Badguy2.rect.y = 440
        Badguy2.boundary_left = 450
        Badguy2.boundary_right = 600
        Badguy2.change_x = 4
        Badguy2.player = self.player
        Badguy2.level = self
        Badguy2.BulletList = BulletList
        self.enemy_list.add(Badguy2)

        if (len(self.pickup_list) == 0) and (len(self.enemy_list)==0):
            gate1.kill()



        
 

 
