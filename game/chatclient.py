from socket import *

def connect_to_server():
    global name
    s = socket()
    host = input("Ange serverns IP-adress:")
    name = input("Ange namn: ")
    port = 12345
    s.connect((host, port))
    return s
conn = connect_to_server()

import tkinter as tk
root = tk.Tk()
root.geometry('300x100')
e = tk.Entry(root, bd = 0, width = 41)
e.place(anchor = tk.CENTER, x = 125, y = 90)
lbl = tk.Label(root)
lbl.place(anchor = tk.CENTER, x = 150, y = 5)
b = tk.Button(root, text ="Skicka", width = 5)

def click_handler(self):
    msg = f'{name}: {e.get()}'
    b = msg.encode("utf-16")
    conn.send(b)
    e.delete(0, 100)

b.bind("<Button-1>", click_handler)
b.place(anchor = tk.CENTER, x = 275, y = 90)

def receiver_thread():
    while True:
        b = conn.recv(1024)
        msg = b.decode("utf-16")
        lbl["text"] = msg
from _thread import *
start_new_thread(receiver_thread, ())
root.mainloop()
