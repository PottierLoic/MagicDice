"""
Game class
"""

from board import Board

class Game:
    def __init__(self):
        self.board1 = Board()
        self.board2 = Board()
        self.blocks = []

    def spawnBlock(self):
        pass

