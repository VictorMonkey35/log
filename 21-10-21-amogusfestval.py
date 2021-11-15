import tkinter as tk
import os
from tkinter.constants import BOTH, YES
os.system('cls')
guestNames = []
guestAges = []

def register():
    if name.get() == '':
        pass
    else:
        os.system('cls')
        guestNames.append(name.get())
        guestAges.append(age.get())
        name.delete(0, 1000)
        age.delete(0,1000)
        age.insert(0, '18')
        print(guestNames)
        print(guestAges)

window = tk.Tk()
window.geometry('600x600')

bg = tk.Canvas(window)
bg.pack(expand=YES, fill=BOTH)
img = tk.PhotoImage(file='material/among.png')
bg.create_image(image=img)

text = tk.Label(window, text='''Welcome to the Amogus Festival™!
Please register yourself.''', anchor=tk.CENTER)
text.pack()

name = tk.Entry(window, bd=5, text='name',)
name.pack()

age = tk.Spinbox(window, from_=18, to=80)
age.pack()

reg = tk.Button(window, text='register', command=register)
reg.pack()

window.mainloop()

amongus = tk.Tk()

os.system('cls')
input()