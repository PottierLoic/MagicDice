"""
Dices class
"""

# Basic libraries
import time

# Local libraries
from constants import *

class Dice:
    def __init__(self) -> None:
        self.dot = 1
        self.projectiles = []
        self.fireDelay = 0
        self.delay = time.time()*1000

    def fire(self):
        if (time.time()*1000 - self.delay) > self.fireDelay:
            self.projectiles.append([self.x, self.y, 0])
            self.delay = time.time()*1000

class FireDice(Dice):
    def __init__(self) -> None:
        super().__init__()
        self.type = "fire"
        self.attack_dmg = FIRE_DICE_ATCK_DMG
        self.color = FIRE_DICE_COLOR
    
    def getColor(self):
        return self.color



    