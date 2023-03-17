"""
Game class
"""

# Basic libraries
import time

# Local libraries
from player import Player
from block import Block
from constants import *

class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.blocks = []
        self.lastSpawn = time.time()*1000

    def update(self):
        self.spawnBlock()
        for block in self.blocks:
            block.move()


    def spawnBlock(self):
        if (time.time()*1000 - self.lastSpawn) > BLOCK_SPAWN_DELAY:
            self.blocks.append(Block())
            self.lastSpawn = time.time()*1000

