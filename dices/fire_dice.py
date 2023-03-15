"""
Fire dice class
"""

# Basic libraries

# File imports
from dices.dice import Dice

class FireDice(Dice):
    def __init__(self) -> None:
        self.__init__()
        self.attack_dmg = 5
        self.color = "red"
