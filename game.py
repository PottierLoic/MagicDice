"""
Game class
"""

from player import Player

class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.blocks = []

    def spawnBlock(self):
        pass

