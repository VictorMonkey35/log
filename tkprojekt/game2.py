import tkinter as tk
import time as t

arena = tk.Tk()
arena.geometry('900x540')

rockimg = tk.PhotoImage(file = 'tkprojekt/bilder/rock.png')
rockimg = rockimg.subsample(7,7)
paperimg = tk.PhotoImage(file = 'tkprojekt/bilder/paper.png')
paperimg = paperimg.subsample(11,11)
scissorsimg = tk.PhotoImage(file = 'tkprojekt/bilder/scissors.png')
scissorsimg = scissorsimg.subsample(10,10)
tableimg = tk.PhotoImage(file = 'tkprojekt/bilder/table.png')
jonasimg = tk.PhotoImage(file = 'tkprojekt/bilder/Jonas.png')

rockY = 450
paperY = 450
scissorsY = 450

rvar = 0
pvar = 0
svar = 0

canvas = tk.Canvas(arena, width = 900, height = 540, bg = 'grey', bd = 0)
canvas.pack()

def rockf():
    global rvar, pvar, svar
    rvar = 1
    pvar = 0
    svar = 0

def paperf():
    global rvar, pvar, svar
    rvar = 0
    pvar = 1
    svar = 0

def scissorsf():
    global rvar, pvar, svar
    rvar = 0
    pvar = 0
    svar = 1

def draw():
    global rockY, paperY, scissorsY
    canvas.create_image(450, 240, anchor = tk.CENTER, image = jonasimg)
    canvas.create_image(450, 600, anchor = tk.CENTER, image = tableimg)
    canvas.create_image(200, rockY, anchor = tk.CENTER, image = rockimg)
    canvas.create_image(450, paperY, anchor = tk.CENTER, image = paperimg)
    canvas.create_image(700, scissorsY, anchor = tk.CENTER, image = scissorsimg)
    rockY = 450 - 8 * rvar
    paperY = 450 - 8 * pvar
    scissorsY = 450 - 8 * svar


def gameloop():
    canvas.delete("all")
    draw()
    canvas.update()
    arena.after(17, func = gameloop)

rockb = tk.Button(arena, text = 'play rock', bd = 1, command = rockf)
rockb.place(anchor = tk.CENTER, x = 200, y = 517)

paperb = tk.Button(arena, text = 'play paper', bd = 1, command = paperf)
paperb.place(anchor = tk.CENTER, x = 450, y = 517)

scissorsb = tk.Button(arena, text = 'play scissors', bd = 1, command = scissorsf)
scissorsb.place(anchor = tk.CENTER, x = 700, y = 517)

gameloop()

arena.mainloop()