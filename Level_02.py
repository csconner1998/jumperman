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


class Level_02(Level):
 
    def __init__(self, player, backround, BulletList):
 
        # Call the parent constructor
        Level.__init__(self, player, backround, BulletList)
 
        self.level_limit = -3500
 
        # Array with width, height, x, and y of platform
        level = [[210, 30, 100, 570],
                 [210, 50, 500, 500],
                 [210, 50, 800, 400],
                 [210, 50, 1100, 300],
                 [210, 50, 1400, 200],
                 [300, 50, 1700, 100],
                 [300, 50, 2200, 100],
                 [300, 50, 2700, 300],
                 [300, 50, 3200, 400],
                 ]
        
        pickups = [[ 830, 340],
                   [ 1440, 140],
                   [ 3260, 340]]
    
 
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

        block = MovingPlatform(210, 50)
        block.rect.x = 3600
        block.rect.y = 300
        block.boundary_left = 3600
        block.boundary_right = 4200
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        Badguy1 = MovingEnemy()
        Badguy1.rect.x = 500
        Badguy1.rect.y = 444
        Badguy1.boundary_left = 500
        Badguy1.boundary_right = 640
        Badguy1.change_x = 3
        Badguy1.player = self.player
        Badguy1.level = self
        Badguy1.BulletList = BulletList
        self.enemy_list.add(Badguy1)

        Badguy2 = MovingEnemy()
        Badguy2.rect.x = 1100
        Badguy2.rect.y = 244
        Badguy2.boundary_left = 1100
        Badguy2.boundary_right = 1240
        Badguy2.change_x = 2
        Badguy2.player = self.player
        Badguy2.level = self
        Badguy2.BulletList = BulletList
        self.enemy_list.add(Badguy2)

        Badguy3 = MovingEnemy()
        Badguy3.rect.x = 1700
        Badguy3.rect.y = 44
        Badguy3.boundary_left = 1700
        Badguy3.boundary_right = 1940
        Badguy3.change_x = 4
        Badguy3.player = self.player
        Badguy3.level = self
        Badguy3.BulletList = BulletList
        self.enemy_list.add(Badguy3)

        Badguy4 = MovingEnemy()
        Badguy4.rect.x = 2700
        Badguy4.rect.y = 240
        Badguy4.boundary_left = 2700
        Badguy4.boundary_right = 2940
        Badguy4.change_x = 4
        Badguy4.player = self.player
        Badguy4.level = self
        Badguy4.BulletList = BulletList
        self.enemy_list.add(Badguy4)

        flag = Flag()
        flag.rect.x = 4400
        flag.rect.y = 540
        self.flag_list.add(flag)

        gate1 = Gate()
        gate1.rect.x = 4340
        gate1.rect.y = 0
        gate1.player = self.player
        self.gate_list.add(gate1)
        
        if (len(self.pickup_list) == 0) and (len(self.enemy_list)==0):
            gate1.kill()

 
