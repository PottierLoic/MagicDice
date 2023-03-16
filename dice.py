"""
Dices class
"""

class Dice:
    def __init__(self) -> None:
        self.dot = 1

class FireDice(Dice):
    def __init__(self) -> None:
        self.__init__()
        self.type = "fire"
        self.attack_dmg = 5
        self.color = "red"


    