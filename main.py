"""
Magic Dice (random dice clone)
Author: Loïc Pottier
Creation date: 15/03/2023
"""

# Basic libraries
from tkinter import *
from PIL import ImageTk, Image

# File imports
from constants import *
from game import Game

def draw():
    canvas.delete("all")
    # Draw background
    canvas.create_image(0, 0, anchor=NW, image=backgroundImg)
    # Draw bottom board and its dices
    for i in range(len(g.player1.board)):
        for j in range(len(g.player1.board[i])):
            if g.player1.board[i][j] == None:
                pass
            else:
                canvas.create_rectangle(200 + int(j*300/5), 500 + int(i*200/3), 200 + int((j+1)*300/5), 500 + int((i+1)*200/3), fill=g.player1.board[i][j].color)
                canvas.create_text(200 + int((j+0.5)*300/5), 500 + int((i+0.5)*200/3), text=g.player1.board[i][j].dot, font=("Arial", 20), fill="white")
    # draw blocks
    for block in g.blocks:
        canvas.create_rectangle(block.x - BLOCK_SIZE / 2, block.y - BLOCK_SIZE / 2, block.x + BLOCK_SIZE / 2, block.y + BLOCK_SIZE / 2, fill=block.color)
    # draw projectiles
    for i in range(len(g.player1.board)):
        for j in range(len(g.player1.board[i])):
            if g.player1.board[i][j] == None:
                pass
            else:
                for projectile in g.player1.board[i][j].projectiles:
                    canvas.create_oval(projectile[0] - PROJECTILE_SIZE / 2, projectile[1] - PROJECTILE_SIZE / 2, projectile[0] + PROJECTILE_SIZE / 2, projectile[1] + PROJECTILE_SIZE / 2, fill=g.player1.board[i][j].color)

def frame():
    draw()
    g.update()
    window.after(1, frame)

if __name__ == "__main__":
    g = Game()
    
    window = Tk()
    window.title("Magic Dice")
    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
    canvas.pack()
    window.update()

    # Images
    backgroundImg = ImageTk.PhotoImage(Image.open("img/background.png"))
 
    # keybinds
    window.bind("<space>", lambda event: g.player1.addDice())

    frame()

    window.mainloop()