#Adala Airlines

#registrera/logga in
#logga in som admin för att lägga till flights

#städer som klasser
#stockholm
#madrid
#paris
#new york
#rio de janeiro
#tokyo
#dubai
#kairo

#flygresor som klasser, olika säten som sub klasser

#passagerare som klasser, med namn och ålder

#economy class, adala plus, bussines class

import mysql.connector
import tkinter as tk
import time as t
import _thread as th
import socket as so

#dataBase = mysql.connector.connect(host = 'loclahost' , user = 'root' , password = '' , database = 'victorsdatabas')

#mycursor = dataBase.cursor()

tickval = 0
menu = True
booking = False
date = 4

months = ['Januari','Februari','Mars','April','Maj','Juni','Juli','Augusti','September','Oktober','November','December']

c = tk.Tk()

adalaLogo1 = tk.PhotoImage(file = 'slutarbete/bilder/adalaLogo1.png')
madrid = tk.PhotoImage(file = 'slutarbete/bilder/madrid.png')
newyork = tk.PhotoImage(file = 'slutarbete/bilder/newyork.png')
rio = tk.PhotoImage(file = 'slutarbete/bilder/rio.png')
whitebox = tk.PhotoImage(file = 'slutarbete/bilder/whitebox.png')

rio = rio.zoom(1,7)
rio = rio.subsample(1,6)
whitebox = whitebox.subsample(6,5)

def register():
    usernametitle.place_forget()
    username.place_forget()
    passwordtitle.place_forget()
    password.place_forget()
    loginb.place_forget()
    registertxt.place_forget()
    registerb.place_forget()

    usernametitle.place(anchor = tk.CENTER , x = 415 , y = 215)
    username.place(anchor = tk.CENTER , x = 480 , y = 235)
    fnametitle.place(anchor = tk.CENTER , x = 415 , y = 255)
    fname.place(anchor = tk.CENTER , x = 480 , y = 275)
    lnametitle.place(anchor = tk.CENTER , x = 415 , y = 295)
    lname.place(anchor = tk.CENTER , x = 480 , y = 315)
    passwordtitle.place(anchor = tk.CENTER , x = 415 , y = 335)
    password.place(anchor = tk.CENTER , x = 480 , y = 355)
    cAccountb.place(anchor = tk.CENTER , x = 480 , y = 395)
    backb.place(anchor = tk.CENTER , x = 330 , y = 85)

def login():
    global menu, booking
    usernametitle.place_forget()
    username.place_forget()
    passwordtitle.place_forget()
    password.place_forget()
    loginb.place_forget()
    registertxt.place_forget()
    registerb.place_forget()
    menu = False
    booking = True
    start()

def loginscreen():
    usernametitle.place_forget()
    username.place_forget()
    fnametitle.place_forget()
    fname.place_forget()
    lnametitle.place_forget()
    lname.place_forget()
    passwordtitle.place_forget()
    password.place_forget()
    cAccountb.place_forget()
    backb.place_forget()

    usernametitle.place(anchor = tk.CENTER , x = 415 , y = 215)
    username.place(anchor = tk.CENTER , x = 480 , y = 235)
    passwordtitle.place(anchor = tk.CENTER , x = 415 , y = 255)
    password.place(anchor = tk.CENTER , x = 480 , y = 275)
    loginb.place(anchor = tk.CENTER , x = 480 , y = 315)
    registertxt.place(anchor = tk.CENTER , x = 455 , y = 440)
    registerb.place(anchor = tk.CENTER , x = 544 , y = 441)

def dateup():
    global date
    if date == 12:
        date = 1
        dtext.config(text = months[date-1])
    
    else:
        date += 1
        dtext.config(text = months[date-1])

def datedown():
    global date
    if date == 1:
        date = 12
        dtext.config(text = months[date-1])
    
    else:
        date -= 1
        dtext.config(text = months[date-1])
    


canvas = tk.Canvas(c , bg = 'lightgrey' , width = 960 ,  height = 600 , bd = 0)
canvas.pack()

usernametitle = tk.Label(c , text = 'Username' , bd = 0 , bg = 'white')
username = tk.Entry(c , width = 30 , bd = 0 , bg = 'lightgrey')

passwordtitle = tk.Label(c , text = 'Password' , bg = 'white' , bd = 0)
password = tk.Entry(c , width = 30 , bd = 0 , bg = 'lightgrey')

loginb = tk.Button(c , text = 'Log in' , bd = 0 , command = login)
cAccountb = tk.Button(c , text = 'Create account' , bd = 0 , command = loginscreen)
backb = tk.Button(c , text = '<-' , bd = 0 , command = loginscreen , bg = 'white')

registertxt = tk.Label(c , text = 'Dont have an account?' , bd = 0 , bg = 'white')
registerb = tk.Button(c , text = 'Register!' , bd = 0 , bg = 'white' , command = register , fg = 'blue')

fnametitle = tk.Label(c , text = 'First name' , bd = 0 , bg = 'white')
fname = tk.Entry(c , width = 30 , bd = 0 , bg = 'lightgrey')

lnametitle = tk.Label(c , text = 'Last name' , bd = 0 , bg = 'white')
lname = tk.Entry(c , width = 30 , bd = 0 , bg = 'lightgrey')


#deklarerar elementen för "top info rutan"
mFrame = tk.Frame(c , bg = 'orange' , bd = 0 , height = 60 , width = 964)


#deklarerar elementen för "location rutan"
LocationVarF1 = tk.IntVar()
LocationVarF2 = tk.IntVar()
LocationVarF3 = tk.IntVar()
LocationVarF4 = tk.IntVar()
LocationVarF5 = tk.IntVar()
LocationVarF6 = tk.IntVar()

LocationVarT1 = tk.IntVar()
LocationVarT2 = tk.IntVar()
LocationVarT3 = tk.IntVar()
LocationVarT4 = tk.IntVar()
LocationVarT5 = tk.IntVar()
LocationVarT6 = tk.IntVar()

lFrame = tk.Frame(c , bg = 'green' , bd = 0 , height = 540 , width = 210)
toText = tk.Label(lFrame , bg = 'white' , bd = 0 , text = 'From')
fromText = tk.Label(lFrame , bg = 'white' , bd = 0 , text = 'From')

flb1 = tk.Checkbutton(lFrame, text = "Stockholm", variable = LocationVarF1, onvalue = 1, offvalue = 0)
flb2 = tk.Checkbutton(lFrame, text = "Madrid", variable = LocationVarF2, onvalue = 1, offvalue = 0)
flb3 = tk.Checkbutton(lFrame, text = "Paris", variable = LocationVarF3, onvalue = 1, offvalue = 0)
flb4 = tk.Checkbutton(lFrame, text = "Dubai", variable = LocationVarF4, onvalue = 1, offvalue = 0)
flb5 = tk.Checkbutton(lFrame, text = "New York", variable = LocationVarF5, onvalue = 1, offvalue = 0)
flb6 = tk.Checkbutton(lFrame, text = "Tokyo", variable = LocationVarF6, onvalue = 1, offvalue = 0)

tlb1 = tk.Checkbutton(lFrame, variable = LocationVarT1, onvalue = 1, offvalue = 0)
tlb2 = tk.Checkbutton(lFrame, variable = LocationVarT2, onvalue = 1, offvalue = 0)
tlb3 = tk.Checkbutton(lFrame, variable = LocationVarT3, onvalue = 1, offvalue = 0)
tlb4 = tk.Checkbutton(lFrame, variable = LocationVarT4, onvalue = 1, offvalue = 0)
tlb5 = tk.Checkbutton(lFrame, variable = LocationVarT5, onvalue = 1, offvalue = 0)
tlb6 = tk.Checkbutton(lFrame, variable = LocationVarT6, onvalue = 1, offvalue = 0)


#deklarerar elementen för "biljettklass rutan"
cFrame = tk.Frame(c , bg = 'blue' , bd = 0 , height = 80 , width = 460)


#deklarerar elementen för "datum rutan"
dFrame = tk.Frame(c , bg = 'red' , bd = 0 , height = 540 , width = 300)
bdbutton = tk.Button(dFrame , text = '<-' , command = datedown , bd = 0 , bg = 'white')
fdbutton = tk.Button(dFrame , text = '->' , command = dateup , bd = 0 , bg = 'white')
dtext = tk.Label(dFrame , text = months[date-1])


#deklarerar elementen för "sökresultat rutan"
fFrame = tk.Frame(c , bg = 'pink' , bd = 0 , height = 460 , width = 460)


#placerar ut alementen för loggin sidan
usernametitle.place(anchor = tk.CENTER , x = 415 , y = 215)
username.place(anchor = tk.CENTER , x = 480 , y = 235)
passwordtitle.place(anchor = tk.CENTER , x = 415 , y = 255)
password.place(anchor = tk.CENTER , x = 480 , y = 275)
loginb.place(anchor = tk.CENTER , x = 480 , y = 315)
registertxt.place(anchor = tk.CENTER , x = 455 , y = 440)
registerb.place(anchor = tk.CENTER , x = 544 , y = 441)


#gör så att variabeln tickvar ökar med 1 i värde, variablen behandlar positionen för bakgrundsbilderna.
def tick():
    global tickval
    if tickval == 2880:
        tickval = 0
    else:
        tickval += 1


#innehåller allt som ska ske i loopen, alltså ritas var 17:e sekund.
def draw():
    if menu == True:
        canvas.create_image(480 - tickval , 310 , anchor = tk.CENTER , image = madrid)
        canvas.create_image(1440 - tickval , 310 , anchor = tk.CENTER , image = newyork)
        canvas.create_image(2400 - tickval , 310 , anchor = tk.CENTER , image = rio)
        canvas.create_image(3360 - tickval , 310 , anchor = tk.CENTER , image = madrid)

        canvas.create_image(480 , 270 , anchor = tk.CENTER , image = whitebox)
        canvas.create_image(480 , 155 , anchor = tk.CENTER , image = adalaLogo1)
    
    if booking == True:
        pass
 

 #ser till att programmet uppdateras var 17:e millisekund.
def loop():
    canvas.delete('all')
    draw()
    if menu == True:
        tick()
    canvas.update()
    c.after(17 , func = loop)


#bygger upp hemsidan.
def start():
    mFrame.place(anchor = tk.NW , x = 0 , y = 0)

    lFrame.place(anchor = tk.NW , x = 0 , y = 60)
    toText.place(anchor = tk.CENTER , x = 20 , y = 20)
    fromText.place(anchor = tk.CENTER , x = 60 , y = 20)
    flb1.place(anchor = tk.NW , x = 80 , y = 40)
    flb2.place(anchor = tk.NW , x = 80 , y = 60)
    flb3.place(anchor = tk.NW , x = 80 , y = 80)
    flb4.place(anchor = tk.NW , x = 80 , y = 100)
    flb5.place(anchor = tk.NW , x = 80 , y = 120)
    flb6.place(anchor = tk.NW , x = 80 , y = 140)
    tlb1.place(anchor = tk.NW , x = 160 , y = 40)
    tlb2.place(anchor = tk.NW , x = 160 , y = 60)
    tlb3.place(anchor = tk.NW , x = 160 , y = 80)
    tlb4.place(anchor = tk.NW , x = 160 , y = 100)
    tlb5.place(anchor = tk.NW , x = 160 , y = 120)
    tlb6.place(anchor = tk.NW , x = 160 , y = 140)

    cFrame.place(anchor = tk.NW , x = 210 , y = 60)

    dFrame.place(anchor = tk.NW , x = 670 , y = 60)
    bdbutton.place(anchor = tk.CENTER , x = 100 , y = 300)
    fdbutton.place(anchor = tk.CENTER , x = 200 , y = 300)
    dtext.place(anchor = tk.CENTER , x = 150 , y = 250)

    fFrame.place(anchor = tk.NW , x = 210 , y = 140)


#startar loopen
loop()


#markerar slutet för tk-fönstret
c.mainloop()