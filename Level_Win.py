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
from Box import Box

class Level_Win(Level):
 
    def __init__(self, player, backround, BulletList):
 
        # Call the parent constructor
        Level.__init__(self, player, backround, BulletList)
 
        self.level_limit = -1300

        # Array with width, height, x, and y of platform
        level = [[120, 30, 50, 570],
                 [30, 200, 50, 400],
                 [30, 200, 160, 400],
                 ]
        # Array with x and y of text
        Winz = [[50, 100],
                [50, 150],
                [50, 200],
                [50, 250],
                [50, 300],
                [100, 350],
                [150, 350],
                [200, 100],
                [200, 150],
                [200, 200],
                [200, 250],
                [200, 300],
                [250, 350],
                [300, 350],
                [350, 100],
                [350, 150],
                [350, 200],
                [350, 250],
                [350, 300],
                [500, 100],
                [500, 150],
                [500, 200],
                [500, 250],
                [500, 300],
                [500, 350],
                [650, 100],
                [650, 150],
                [650, 200],
                [650, 250],
                [650, 300],
                [650, 350],
                [700, 100],
                [700, 150],
                [750, 200],
                [800, 250],
                [850, 300],
                [850, 350],
                [900, 100],
                [900, 150],
                [900, 200],
                [900, 250],
                [900, 300],
                [900, 350],
                ]
               
        
 
        # Go through the array above and add platforms
        for platform in level:
            block = Box(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for platform in Winz:
            block = Win()
            block.rect.x = (platform[0] + 340)  
            block.rect.y = platform[1]
            block.player = self.player
            self.win_list.add(block)





        
 

 
