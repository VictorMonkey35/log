#stensaxpåse.

import tkinter as tk
import time as t
import random as r
from typing import Counter

class enemy:
    def __init__(self, counter, draw):
        self.counter = counter
        self.draw = draw

    def drag(self, counter, draw):
        if r.random() > counter:
            if r.random() > draw:
                pass
            else:
                pass
        else:
            pass

HEIGHT = 600
WIDTH = 800

menu = tk.Tk()

canvas = tk.Canvas(menu, height = HEIGHT, width = WIDTH)
canvas.pack()

title = tk.Label(menu, text = 'Välkommen till StenSaxPåse RolePlay')
#title.place(anchor = tk.CENTER, height = HEIGHT/10, width = WIDTH/2)

frame1 = tk.Frame(menu, height = 2*HEIGHT/3, width = WIDTH/4, bd = 0, bg = 'red')
frame1.place(anchor = tk.CENTER, x = 2*WIDTH/8, y = HEIGHT/2)
frame1.pack_propagate(0)
canvas1 = tk.Canvas(frame1)
canvas1.pack()
img1 = tk.PhotoImage(file= 'tkprojekt/bilder/jonas.png')
canvas.create_image(0,0, anchor=tk.NW, image=img1)
playb1 = tk.Button(frame1, text = 'PLAY', bg = 'white')
playb1.pack()

frame2 = tk.Frame(menu, height = 2*HEIGHT/3, width = WIDTH/4, bd = 0, bg = 'green')
frame2.place(anchor = tk.CENTER, x = 4*WIDTH/8, y = HEIGHT/2)
frame2.pack_propagate(0)
playb2 = tk.Button(frame2, text = 'PLAY')
playb2.pack()

frame3 = tk.Frame(menu, height = 2*HEIGHT/3, width = WIDTH/4, bd = 0, bg = 'blue')
frame3.place(anchor = tk.CENTER, x = 6*WIDTH/8, y = HEIGHT/2)
frame3.pack_propagate(0)
playb2 = tk.Button(frame3, text = 'PLAY')
playb2.pack()

menu.mainloop()

