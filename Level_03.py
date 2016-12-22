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

class Level_03(Level):
 
    def __init__(self, player, backround, BulletList):
 
        # Call the parent constructor
        Level.__init__(self, player, backround, BulletList)
 
        self.level_limit = -2400

        # Array with width, height, x, and y of platform
        level = [[210, 30, 100, 570],
                 [150, 50, 750, 150],
                 [250, 50, 1100, 500],
                 [210, 40, 2100, 150],
                 [240, 40, 2050, 500]
                 ]
        # Array with x and y of
        pickups = [[ 770, 20],
                   [ 1500, 40],
                   [ 1150, 440]
                   ]
        
 
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
        flag.rect.x = 3300
        flag.rect.y = 540
        self.flag_list.add(flag)
    

        gate1 = Gate()
        gate1.rect.x = 3240
        gate1.rect.y = 0
        gate1.player = self.player
        self.gate_list.add(gate1)

        block1 = MovingPlatform(300, 50)
        block1.rect.x = 350
        block1.rect.y = 300
        block1.boundary_top = 150
        block1.boundary_bottom = 570
        block1.change_y = 2
        block1.player = self.player
        block1.level = self
        self.platform_list.add(block1)

        block2 = MovingPlatform(200, 40)
        block2.rect.x = 1000
        block2.rect.y = 100
        block2.boundary_left = 1000
        block2.boundary_right = 1700
        block2.change_x = 3
        block2.player = self.player
        block2.level = self
        self.platform_list.add(block2)

        block3 = MovingPlatform(200, 30)
        block3.rect.x = 2400
        block3.rect.y = 150
        block3.boundary_top = 150
        block3.boundary_bottom = 550 
        block3.change_y = 2
        block3.player = self.player
        block3.level = self
        self.platform_list.add(block3)

        block4 = MovingPlatform(200, 40)
        block4.rect.x = 1600
        block4.rect.y = 500
        block4.boundary_left = 1400
        block4.boundary_right = 1750
        block4.change_x = 2
        block4.player = self.player
        block4.level = self
        self.platform_list.add(block4)

        block5 = MovingPlatform(200, 40)
        block5.rect.x = 2650
        block5.rect.y = 550
        block5.boundary_left = 2650
        block5.boundary_right = 3500
        block5.change_x = 2
        block5.player = self.player
        block5.level = self
        self.platform_list.add(block5)
        
        Badguy1 = MovingEnemy()
        Badguy1.rect.x = 800
        Badguy1.rect.y = 90
        Badguy1.boundary_left = 740
        Badguy1.boundary_right = 850
        Badguy1.change_x = 1
        Badguy1.player = self.player
        Badguy1.level = self
        Badguy1.BulletList = BulletList
        self.enemy_list.add(Badguy1)

        Badguy2 = Enemy()
        Badguy2.rect.x = 2250
        Badguy2.rect.y = 90
        Badguy2.player = self.player
        Badguy2.level = self
        Badguy2.BulletList = BulletList
        self.enemy_list.add(Badguy2)

        if (len(self.pickup_list) == 0) and (len(self.enemy_list)==0):
            gate1.kill()


        
 

 
