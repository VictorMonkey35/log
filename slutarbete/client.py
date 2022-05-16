import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="victorsdatabas"
)

mycursor = mydb.cursor()

print("Uppkopplad till databasen!")


import tkinter as tk
import time as t
import _thread as th
import socket as so
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

tickval = 0
menu = True
booking = False
date = 4

months = ['Januari','Februari','Mars','April','Maj','Juni','Juli','Augusti','September','Oktober','November','December']

c = tk.Tk()

adalaLogo1 = tk.PhotoImage(file = 'slutarbete/bilder/adalaLogo1.png')
adalaLogo2 = tk.PhotoImage(file = 'slutarbete/bilder/adalaLogo2.png')
madrid = tk.PhotoImage(file = 'slutarbete/bilder/madrid.png')
newyork = tk.PhotoImage(file = 'slutarbete/bilder/newyork.png')
rio = tk.PhotoImage(file = 'slutarbete/bilder/rio.png')
whitebox = tk.PhotoImage(file = 'slutarbete/bilder/whitebox.png')
profileimg = tk.PhotoImage(file = 'slutarbete/bilder/profileimg.png')
searchimg = tk.PhotoImage(file = 'slutarbete/bilder/searchimg.png')

rio = rio.zoom(1,7)
rio = rio.subsample(1,6)
whitebox = whitebox.subsample(6,5)
adalaLogo2 = adalaLogo2.subsample(5,5)
profileimg = profileimg.subsample(7,7)
searchimg = searchimg.subsample(8,8)

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

def createAccount():
    if username.get() != '' and fname.get() != '' and lname.get() != '' and password.get() != '':
        accountlist = []
        accountlist.append(username.get())
        accountlist.append(fname.get())
        accountlist.append(lname.get())
        accountlist.append(password.get())
        print(accountlist)

        msg = accountlist
        b = msg.encode("utf-16")
        conn.send(b)

        """sql = 'INSERT INTO `users` (`UserName`, `Firstname`, `Surname`, `Password`) VALUES (%s, %s, %s, %s)'
        val = (username.get(), fname.get(), lname.get(), password.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        # Läsa från databasen
        mycursor.execute("SELECT * FROM users")
        myresult = mycursor.fetchall()
        loginscreen()
        for x in myresult:
            print(x)"""

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
    
def Search():
    pass

canvas = tk.Canvas(c , bg = 'black' , width = 960 ,  height = 600 , bd = 0)
canvas.pack()

usernametitle = tk.Label(c , text = 'Username' , bd = 0 , bg = 'white')
username = tk.Entry(c , width = 30 , bd = 0 , bg = 'lightgrey')

passwordtitle = tk.Label(c , text = 'Password' , bg = 'white' , bd = 0)
password = tk.Entry(c , width = 30 , bd = 0 , bg = 'lightgrey', show = '*')

loginb = tk.Button(c , text = 'Log in' , bd = 0 , command = login)
cAccountb = tk.Button(c , text = 'Create account' , bd = 0 , command = createAccount)
backb = tk.Button(c , text = '<-' , bd = 0 , command = loginscreen , bg = 'white')

registertxt = tk.Label(c , text = 'Dont have an account?' , bd = 0 , bg = 'white')
registerb = tk.Button(c , text = 'Register!' , bd = 0 , bg = 'white' , command = register , fg = 'blue' , activebackground = 'white')

fnametitle = tk.Label(c , text = 'First name' , bd = 0 , bg = 'white')
fname = tk.Entry(c , width = 30 , bd = 0 , bg = 'lightgrey')

lnametitle = tk.Label(c , text = 'Last name' , bd = 0 , bg = 'white')
lname = tk.Entry(c , width = 30 , bd = 0 , bg = 'lightgrey')


#deklarerar elementen för "top info rutan"
mFrame = tk.Frame(c , bg = 'orange' , bd = 0 , height = 59 , width = 964)
mButton = tk.Button(mFrame , image = adalaLogo2 , bd = 0 , bg = 'orange' , activebackground = 'orange')
pButton = tk.Button(mFrame , image = profileimg , bg = 'orange' , bd = 0 , activebackground = 'orange')


#deklarerar elementen för "biljettklass rutan"
cFrame = tk.Frame(c , bg = 'white' , bd = 0 , height = 80 , width = 669)

searchB = tk.Button(cFrame , bg = 'white' , activebackground = 'white' , bd = 0 , image = searchimg , command = Search)

economy = tk.IntVar()
plus = tk.IntVar()
bussines = tk.IntVar()

economyB = tk.Checkbutton(cFrame , bg = 'white' , bd = 0 , text = 'Economy')
plusB = tk.Checkbutton(cFrame , bg = 'white' , bd = 0 , text = 'Plus')
bussinesB = tk.Checkbutton(cFrame , bg = 'white' , bd = 0 , text = 'Bussines')


#separation frames för estetiska skäl
sFrame1 = tk.Frame(c , bg = 'grey' , bd = 0 , height = 540 , width = 1)
sFrame2 = tk.Frame(c , bg = 'grey' , bd = 0 , height = 1 , width = 964)


#deklarerar variabler för location checkboxes
FromStockholm = tk.IntVar()
FromMadrid = tk.IntVar()
FromParis = tk.IntVar()
FromDubai = tk.IntVar()
FromNewYork = tk.IntVar()
FromTokyo = tk.IntVar()

ToStockholm = tk.IntVar()
ToMadrid = tk.IntVar()
ToParis = tk.IntVar()
ToDubai = tk.IntVar()
ToNewYork = tk.IntVar()
ToTokyo = tk.IntVar()


#deklarerar elementen för "filter rutan"
fFrame = tk.Frame(c , bg = 'white' , bd = 0 , height = 540 , width = 300)

bdbutton = tk.Button(fFrame , text = '<-' , command = datedown , bd = 0 , bg = 'white')
fdbutton = tk.Button(fFrame , text = '->' , command = dateup , bd = 0 , bg = 'white')
dtext = tk.Label(fFrame , text = months[date-1] , bg = 'white')

toText = tk.Label(fFrame , bg = 'white' , bd = 0 , text = 'To')
fromText = tk.Label(fFrame , bg = 'white' , bd = 0 , text = 'From')

StockholmT = tk.Label(fFrame , bg = 'white' , bd = 0 , text = 'Stockholm')
MadridT = tk.Label(fFrame , bg = 'white' , bd = 0 , text = 'Madrid')
ParisT = tk.Label(fFrame , bg = 'white' , bd = 0 , text = 'Paris')
DubaiT = tk.Label(fFrame , bg = 'white' , bd = 0 , text = 'Dubai')
NewYorkT = tk.Label(fFrame , bg = 'white' , bd = 0 , text = 'New York')
TokyoT = tk.Label(fFrame , bg = 'white' , bd = 0 , text = 'Tokyo')

flb1 = tk.Checkbutton(fFrame , variable = FromStockholm , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0)
flb2 = tk.Checkbutton(fFrame , variable = FromMadrid    , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0)
flb3 = tk.Checkbutton(fFrame , variable = FromParis     , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0)
flb4 = tk.Checkbutton(fFrame , variable = FromDubai     , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0)
flb5 = tk.Checkbutton(fFrame , variable = FromNewYork   , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0)
flb6 = tk.Checkbutton(fFrame , variable = FromTokyo     , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0)

tlb1 = tk.Checkbutton(fFrame , variable = ToStockholm   , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0)
tlb2 = tk.Checkbutton(fFrame , variable = ToMadrid      , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0)
tlb3 = tk.Checkbutton(fFrame , variable = ToParis       , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0)
tlb4 = tk.Checkbutton(fFrame , variable = ToDubai       , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0)
tlb5 = tk.Checkbutton(fFrame , variable = ToNewYork     , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0)
tlb6 = tk.Checkbutton(fFrame , variable = ToTokyo       , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0)


#deklarerar elementen för "resultat rutan"
rFrame = tk.Frame(c , bg = 'lightgrey' , bd = 0 , height = 460 , width = 669)
Scroll = tk.Scrollbar(rFrame)


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
    mButton.place(anchor = tk.CENTER , x = 100 , y = 30)
    pButton.place(anchor = tk.CENTER , x = 930 , y = 37)
    
    cFrame.place(anchor = tk.NW , x = 0 , y = 60)
    economyB.place(anchor = tk.CENTER , x = 120 , y = 40)
    plusB.place(anchor = tk.CENTER , x = 260 , y = 40)
    bussinesB.place(anchor = tk.CENTER , x = 400 , y = 40)
    searchB.place(anchor = tk.CENTER , x = 600 , y = 45)

    fFrame.place(anchor = tk.NW , x = 670 , y = 60)
    bdbutton.place(anchor = tk.CENTER , x = 100 , y = 400)
    fdbutton.place(anchor = tk.CENTER , x = 200 , y = 400)
    dtext.place(anchor = tk.CENTER , x = 150 , y = 400)
    toText.place(anchor = tk.CENTER , x = 195 , y = 70)
    fromText.place(anchor = tk.CENTER , x = 110 , y = 70)
    StockholmT.place(anchor = tk.CENTER , x = 150 , y = 120)
    MadridT.place(anchor = tk.CENTER , x = 150 , y = 160)
    ParisT.place(anchor = tk.CENTER , x = 150 , y = 200)
    DubaiT.place(anchor = tk.CENTER , x = 150 , y = 240)
    NewYorkT.place(anchor = tk.CENTER , x = 150 , y = 280)
    TokyoT.place(anchor = tk.CENTER , x = 150 , y = 320)
    flb1.place(anchor = tk.CENTER , x = 110 , y = 120)
    flb2.place(anchor = tk.CENTER , x = 110 , y = 160)
    flb3.place(anchor = tk.CENTER , x = 110 , y = 200)
    flb4.place(anchor = tk.CENTER , x = 110 , y = 240)
    flb5.place(anchor = tk.CENTER , x = 110 , y = 280)
    flb6.place(anchor = tk.CENTER , x = 110 , y = 320)
    tlb1.place(anchor = tk.CENTER , x = 195 , y = 120)
    tlb2.place(anchor = tk.CENTER , x = 195 , y = 160)
    tlb3.place(anchor = tk.CENTER , x = 195 , y = 200)
    tlb4.place(anchor = tk.CENTER , x = 195 , y = 240)
    tlb5.place(anchor = tk.CENTER , x = 195 , y = 280)
    tlb6.place(anchor = tk.CENTER , x = 195 , y = 320)

    sFrame1.place(anchor = tk.NW , x = 669 , y = 60)
    sFrame2.place(anchor = tk.NW , x = 0 , y = 59)

    rFrame.place(anchor = tk.NW , x = 0 , y = 140)
    #Scroll.pack(side = tk.RIGHT , fill = tk.Y)

    Search()


#startar loopen
loop()


#markerar slutet för tk-fönstret
c.mainloop()