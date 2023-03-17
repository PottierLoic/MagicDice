"""
Block class
"""

# Basic libraries
import time

# Local libraries
from constants import *

class Block():
    def __init__(self) -> None:
        self.health = 10
        self.x = 100
        self.y = 800
        self.color = BLOCK_COLOR
        self.movementTimer = time.time()*1000
    
    def move(self):
        if (time.time()*1000 - self.movementTimer) > TIMER:
            if self.y >= 400:
                self.y -= 1
            else:
                self.x += 1