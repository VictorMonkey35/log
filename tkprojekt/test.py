import tkinter as tk
import time
import random as rand
x = tk.Tk()
c = tk.Canvas(x, bg="white", height=720, width=1280)
c.pack()

arrowImg = tk.PhotoImage(file='./projekt/bowsimulator/arrow1.png')
board = tk.PhotoImage(file='./projekt/bowsimulator/board.png')

bowAnimation = [
    tk.PhotoImage(file='./projekt/bowsimulator/bow1.png'), 
    tk.PhotoImage(file='./projekt/bowsimulator/bow2.png'), 
    tk.PhotoImage(file='./projekt/bowsimulator/bow3.png'),
    tk.PhotoImage(file='./projekt/bowsimulator/bow4.png')]

arrowX = 100
arrowY = 500
arrowYVel = 5
run = True


def gameloop():
    global arrowX
    global arrowY
    global arrowYVel
    global run
    c.create_image(100, 500, image=bowAnimation[rand.randint(0,3)])
    c.create_image(arrowX, arrowY, image=arrowImg)

    arrowX = arrowX + 10
    arrowYVel = arrowYVel - 0.1
    arrowY = arrowY + -arrowYVel
    if arrowX >= 1200:
        run = False
    if run:
        c.update()
        time.sleep(1/60)
        c.delete("all")
        gameloop()

gameloop()
x.mainloop()