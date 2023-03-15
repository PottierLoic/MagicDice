"""
Board class
"""

# Basic libraries
import random

# File imports
from dices.fire_dice import FireDice

class Board:
    def __init__(self) -> None:
        self.board = [[0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0]]
        self.deck = [FireDice, FireDice, FireDice, FireDice, FireDice]
        self.addDice()

    # Add dice to board on a random open spot
    def addDice(self):
        open = []
        for i in range(3):
            for j in range(5):
                if self.board[i][j] == 0:
                    open.append((i, j))
        if len(open) == 0:
            return
        else:
            rd = random.choice(open)
            self.board[rd[0]][rd[1]] = random.choice(self.deck)
        
    def __str__(self) -> str:
        return str(self.board)
    