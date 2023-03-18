"""
Player class
"""

# Basic libraries
import random

# File imports
from dice import *

class Player:
    def __init__(self, parent) -> None:
        self.parent = parent
        self.board = [[None, None, None, None, None], 
                      [None, None, None, None, None], 
                      [None, None, None, None, None]]
        self.deck = ["FireDice" for i in range(5)]
        self.gold = 100
        self.cost = 10

    # Add dice to the board on a random open spot
    def addDice(self):
        if self.gold > self.cost:
            open = []
            for i in range(3):
                for j in range(5):
                    if self.board[i][j] == None:
                        open.append((i, j))
            if len(open) == 0:
                return
            else:
                rd = random.choice(open)
                dice = random.choice(self.deck)
                match dice:
                    case "FireDice":
                        self.board[rd[0]][rd[1]] = FireDice(self, 200 + int((rd[1]+0.5)*300/5), 500 + int((rd[0]+0.5)*200/3))
                    case _:
                        pass
                self.gold -= self.cost
            