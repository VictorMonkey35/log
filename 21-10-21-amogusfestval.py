import tkinter as tk
import os
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

text = tk.Label(window, text='''Welcome to the Amogus Festival™!
Please register yourself.''', anchor=tk.CENTER)
text.pack()

name = tk.Entry(window, bd=5, text='name')
name.pack()

age = tk.Spinbox(window, from_=18, to=80)
age.pack()

reg = tk.Button(window, text='register', command=register)
reg.pack()

window.mainloop()

os.system('cls')
for i in range(len(guestAges)):
    print(f'''Deltagare {i+1}: 
Namn: {guestNames[i]}.
Ålder: {guestAges[i]}.
''')
input()