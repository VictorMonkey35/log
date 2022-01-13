import tkinter as tk
import time as t
import random as r

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
jonassub = jonasimg.subsample(7,7)
winimg = tk.PhotoImage(file = 'tkprojekt/bilder/youwin.png')
loseimg = tk.PhotoImage(file = 'tkprojekt/bilder/youlose.png')

jonasscore = 0
playerscore = 0
rockY = 450
paperY = 450
scissorsY = 450
jonasY = 240

rvar = 0
pvar = 0
svar = 0

playvar = 0
runvar = 0

rint = 0

jonasvar = 0
safejonas = 0

canvas = tk.Canvas(arena, width = 900, height = 540, bg = 'grey', bd = 0)
canvas.pack()

def rockf():
    global rvar, pvar, svar, playvar
    rvar = 1
    pvar = 0
    svar = 0
    playvar = 1

def paperf():
    global rvar, pvar, svar, playvar
    rvar = 0
    pvar = 1
    svar = 0
    playvar = 2

def scissorsf():
    global rvar, pvar, svar, playvar
    rvar = 0
    pvar = 0
    svar = 1
    playvar = 3

def play():
    global runvar, playvar
    if playvar != 0:
        runvar = 1
        playb.place_forget()
        rockb.place_forget()
        paperb.place_forget()
        scissorsb.place_forget()
        resetb.place_forget()
        arena.after(2200, func = hismove)

def spawnrb():
    global playerscore, jonasscore
    if playerscore == 3 or jonasscore == 3:
        pass
    else:
        resetb.place(anchor = tk.CENTER, x = 450, y = 400)

def jonasplus():
    global jonasscore
    jonasscore += 1

def playerplus():
    global playerscore
    playerscore += 1

def draw2():
    global playerscore
    playerscore += 0

        
def hismove():
    global rint, jonasvar, jonasscore, playerscore
    jonasvar = 1
    rint = r.randint(1,3)

    if playvar == 1:
        if rint == 1:
            arena.after(1500, func = draw2)
        elif rint == 2:
            arena.after(1500, func = jonasplus)
        elif rint == 3:
            arena.after(1500, func = playerplus)

    elif playvar == 2:
        if rint == 1:
            arena.after(1500, func = playerplus)
        elif rint == 2:
            arena.after(1500, func = draw2)
        elif rint == 3:
            arena.after(1500, func = jonasplus)

    elif playvar == 3:
        if rint == 1:
            arena.after(1500, func = jonasplus)
        elif rint == 2:
            arena.after(1500, func = playerplus)
        elif rint == 3:
            arena.after(1500, func = draw2)

    arena.after(1500, func = spawnrb)

def reset():
    global rockY, paperY, scissorsY, jonasY, rvar, pvar, svar, playvar, runvar, rint, jonasvar, safejonas
    rockb.place(anchor = tk.CENTER, x = 200, y = 517)
    paperb.place(anchor = tk.CENTER, x = 450, y = 517)
    scissorsb.place(anchor = tk.CENTER, x = 700, y = 517)
    playb.place(anchor = tk.CENTER, x = 450, y = 270)

    rockY = 450
    paperY = 450
    scissorsY = 450
    jonasY = 240

    rvar = 0
    pvar = 0
    svar = 0

    playvar = 0
    runvar = 0

    rint = 0

    jonasvar = 0
    safejonas = 0

    resetb.place_forget()

def draw():
    global rvar, pvar, svar, rockY, paperY, scissorsY, jonasY, safejonas, jonasscore, playerscore
    if jonasscore == 3:
        canvas.create_image(450, 270, anchor = tk.CENTER, image = loseimg)
    elif playerscore == 3:
        canvas.create_image(450, 270, anchor = tk.CENTER, image = winimg)
    elif runvar == 0:
        canvas.create_image(450, 240, anchor = tk.CENTER, image = jonasimg)
        canvas.create_image(450, 600, anchor = tk.CENTER, image = tableimg)
        canvas.create_image(200, rockY, anchor = tk.CENTER, image = rockimg)
        canvas.create_image(450, paperY, anchor = tk.CENTER, image = paperimg)
        canvas.create_image(700, scissorsY, anchor = tk.CENTER, image = scissorsimg)
    elif runvar == 1:
        canvas.create_image(450, jonasY, anchor = tk.CENTER, image = jonasimg)
        canvas.create_image(450, 600, anchor = tk.CENTER, image = tableimg)
        if playvar == 1:
            canvas.create_image(200, rockY, anchor = tk.CENTER, image = rockimg)
        elif playvar == 2:
            canvas.create_image(450, paperY, anchor = tk.CENTER, image = paperimg)
        elif playvar == 3:
            canvas.create_image(700, scissorsY, anchor = tk.CENTER, image = scissorsimg)
    if jonasscore == 3:
        canvas.create_text(450, 460, anchor = tk.CENTER, text = f'final score: {jonasscore} - {playerscore} till Jonas.')
    elif playerscore == 3:
        canvas.create_text(450, 460, anchor = tk.CENTER, text = f'final score: {playerscore} - {jonasscore} till dig.')
    else:
        canvas.create_text(50, 25, anchor = tk.CENTER, text = jonasscore)
        canvas.create_text(850, 25, anchor = tk.CENTER, text = playerscore)
    #update rock place
    if rvar == 1:
        if rockY >= 435:
            rockY -= 5
        else:
            pass
    else:
        if rockY == 450:
            pass
        else:
            rockY += 5
    #update paper place
    if pvar == 1:
        if paperY >= 435:
            paperY -= 5
        else:
            pass
    else:
        if paperY == 450:
            pass
        else:
            paperY += 5
    #update scissors place
    if svar == 1:
        if scissorsY >= 435:
            scissorsY -= 5
        else:
            pass
    else:
        if scissorsY == 450:
            pass
        else:
            scissorsY += 5
    
    #update jonas place
    if jonasvar == 1:
        if jonasY < 280 and safejonas == 0:
            jonasY += 8
        elif jonasY > 240:
            safejonas = 1
            jonasY -= 5
    
    if rint == 1 and safejonas == 1:
        if playerscore == 3:
            pass
        elif jonasscore == 3:
            pass
        else:
            canvas.create_image(220, 280, anchor = tk.CENTER, image = rockimg)
    elif rint == 2 and safejonas == 1:
        if playerscore == 3:
            pass
        elif jonasscore == 3:
            pass
        else:
            canvas.create_image(220, 285, anchor = tk.CENTER, image = paperimg)
    elif rint == 3 and safejonas == 1:
        if playerscore == 3:
            pass
        elif jonasscore == 3:
            pass
        else:
            canvas.create_image(220, 290, anchor = tk.CENTER, image = scissorsimg)
    else:
        pass


def gameloop():
    canvas.delete("all")
    draw()
    canvas.update()
    arena.after(17, func = gameloop)

rockb = tk.Button(arena, text = 'rock', bd = 1, command = rockf)
rockb.place(anchor = tk.CENTER, x = 200, y = 517)

paperb = tk.Button(arena, text = 'paper', bd = 1, command = paperf)
paperb.place(anchor = tk.CENTER, x = 450, y = 517)

scissorsb = tk.Button(arena, text = 'scissors', bd = 1, command = scissorsf)
scissorsb.place(anchor = tk.CENTER, x = 700, y = 517)

playb = tk.Button(arena, text = 'play', bd = 1, command = play)
playb.place(anchor = tk.CENTER, x = 450, y = 270)

resetb = tk.Button(arena, text = 'playnext', bd = 1, command = reset)

gameloop()

arena.mainloop()