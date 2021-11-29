#Vacation booker
#Norwegian airshuttle sim
import tkinter as tk
import time as t
import os
from tkinter.constants import ANCHOR, CENTER

HEIGHT = 370
WIDTH = 600

main = tk.Tk()
main.geometry('600x370')

canvas = tk.Canvas(main, height = HEIGHT, width = WIDTH,  bd = 0, bg = 'grey')
canvas.place(x = WIDTH/2, y = HEIGHT/2, anchor = CENTER)
#fin bild som bakgrund

frame = tk.Frame(main, height = HEIGHT/2, width = WIDTH/1.4, bg = 'white')
frame.place(x = WIDTH/2, y = HEIGHT/2, anchor = CENTER)

region = tk.Checkbutton(frame)
region.place(x = 3*WIDTH/(10*1.1), y = 3*HEIGHT/(10*1.1), anchor = CENTER)
#rad högst upp, välj region.

country = tk.Entry(frame)
country.place(x = 2*WIDTH/(10*1.1), y = 2*HEIGHT/(10*1.1), anchor = CENTER)
#antingen skriv eller annan lösning för att hitta land.


main.mainloop()
#justera pris, personer o annat för att hitta flights.
#generera random flights baserat på inputs hittils.
#ha en sökknap. uppdatera då alla variabler o sånt.

browse = tk.Tk()
browse.mainloop()