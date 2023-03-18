"""
Dices class
"""

# Basic libraries
import time
import math

# Local libraries
from constants import *

class Dice:
    def __init__(self, parent, x, y) -> None:
        self.parent = parent
        self.x = x
        self.y = y

        self.dot = 1
        self.projectiles = []
        
        self.fireDelay = time.time()*1000
        self.fireRate = 0

        self.bulletMoveDelay = time.time()*1000

    def update(self):
        self.fire()
        self.moveProjectiles()

    def fire(self):
        if (time.time()*1000 - self.fireDelay) > self.fireRate and len(self.parent.parent.blocks) > 0:
            self.projectiles.append([self.x, self.y])
            self.fireDelay = time.time()*1000

    def moveProjectiles(self):
        if len(self.parent.parent.blocks) > 0:
            if (time.time()*1000 - self.bulletMoveDelay) > BULLET_MOVE_DELAY:
                for projectile in self.projectiles:
                    direction = math.atan2(self.parent.parent.blocks[0].y - projectile[1], self.parent.parent.blocks[0].x - projectile[0])
                    projectile[0] += math.cos(direction)
                    projectile[1] += math.sin(direction)
                self.bulletMoveDelay = time.time()*1000

class FireDice(Dice):
    def __init__(self, parent, x, y) -> None:
        super().__init__(parent, x, y)
        self.type = "fire"
        self.attack_dmg = FIRE_DICE_ATCK_DMG
        self.color = FIRE_DICE_COLOR
        self.fireRate = FIRE_DICE_FIRE_RATE
    
    def getColor(self):
        return self.color



    