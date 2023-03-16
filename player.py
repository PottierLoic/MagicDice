"""
Player class
"""

# Basic libraries
import random

# File imports
from dice import *

class Player:
    def __init__(self) -> None:
        self.board = [[0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0]]
        self.deck = [FireDice for i in range(5)]
        self.gold = 100
        self.cost = 10

    # Add dice to the board on a random open spot
    def addDice(self):
        if self.gold > self.cost:
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
                self.gold -= self.cost
            