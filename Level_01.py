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

class Level_01(Level):
 
    def __init__(self, player, backround, BulletList):
 
        # Call the parent constructor
        Level.__init__(self, player, backround, BulletList)
 
        self.level_limit = -1300

        # Array with width, height, x, and y of platform
        level = [[210, 30, 100, 570],
                 [210, 30, 500, 500],
                 [210, 30, 800, 400],
                 [210, 30, 1120, 280],
                 ]
        # Array with x and y of
        pickups = [[ 900, 340],
                   [ 200, 510],
                   [ 1220, 230]]
        
 
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
        flag.rect.x = 2200
        flag.rect.y = 540
        self.flag_list.add(flag)
    

        gate1 = Gate()
        gate1.rect.x = 2000
        gate1.rect.y = 0
        gate1.player = self.player
        self.gate_list.add(gate1)

        block = MovingPlatform(200, 50)
        block.rect.x = 1350
        block.rect.y = 520
        block.boundary_left = 1350
        block.boundary_right = 2000
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        Badguy1 = MovingEnemy()
        Badguy1.rect.x = 500
        Badguy1.rect.y = 440
        Badguy1.boundary_left = 500
        Badguy1.boundary_right = 640
        Badguy1.change_x = 2
        Badguy1.player = self.player
        Badguy1.level = self
        Badguy1.BulletList = BulletList
        self.enemy_list.add(Badguy1)

        if (len(self.pickup_list) == 0) and (len(self.enemy_list)==0):
            gate1.kill()



        
 

 
