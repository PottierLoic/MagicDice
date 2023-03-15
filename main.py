"""
Magic Dice (random dice clone)
Author: Loïc Pottier
Creation date: 15/03/2023
"""

# Basic libraries
import random
from tkinter import *

# File imports
from constants import *
from board import Board

def draw():
    canvas.delete("all")
    for i in range(len(b.board)):
        for j in range(len(b.board[i])):
            if b.board[i][j] == 0:
                pass
            else:
                canvas.create_rectangle(i*WIDTH/5, j*HEIGHT/3, (i+1)*WIDTH/5, (j+1)*HEIGHT/3, fill="red")



def frame():
    draw()
    window.after(1, frame)

window = Tk()
window.title("Magic Dice")
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()
window.update()

b = Board()

frame()

window.mainloop()