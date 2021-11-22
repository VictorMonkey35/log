import tkinter as tk
import os
from tkinter.constants import BOTH, CENTER, YES
os.system('cls')
guestNames = []
guestAges = []

def register():
    if name.get() == '':
        pass
    elif int(age.get()) <= 17:
        name.delete(0, 1000)
        age.delete(0,1000)
        age.insert(0, '18')
    else:
        os.system('cls')
        guestNames.append(name.get())
        guestAges.append(age.get())
        name.delete(0, 1000)
        age.delete(0,1000)
        age.insert(0, '18')

def done():
    window.destroy()

window = tk.Tk()
window.geometry('300x300')

bg = tk.PhotoImage(file = 'material/amongus.png')
picture = tk.Label(window,image = bg)
picture.place(x=0,y=0)

text = tk.Label(window, text='''Welcome to the Amogus Festival™!
Please register yourself.''', anchor=tk.CENTER)
text.pack()

name = tk.Entry(window, bd=5, text='name',)
name.pack()

age = tk.Spinbox(window, from_=18, to=80)
age.pack()

reg = tk.Button(window, text='Register', command=register, anchor=CENTER)
reg.place(x=150,y=215,anchor=CENTER)

reg = tk.Button(window, text='Done', command=done, anchor=CENTER)
reg.place(x=150,y=245,anchor=CENTER)

window.mainloop()