import tkinter as tk
root = tk.Tk()

bg = tk.PhotoImage(file = 'material/among.png')
label1 = tk.Label(root,image = bg)
label1.place(x=0,y=0)
label1 = tk.Label(root,image = bg)
label1.place(x=0,y=0)

root.mainloop()