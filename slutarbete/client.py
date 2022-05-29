import tkinter as tk
import random as r
from socket import *

def connect_to_server():
    s = socket()
    host = 'localhost'
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
    global menu, booking , myID

    if username.get() != '' and password.get() != '':
        msg = username.get() + ' ' + password.get()
        msg = str(msg)
        makesure = msg.split()
        if len(makesure) == 2:
            b = msg.encode('utf-16')
            conn.send(b)
            b = conn.recv(1024)
            msg = b.decode('utf-16')
            if msg == 'NotLoggedIn':
                pass
            else:
                myID = msg
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
        
        msg = username.get() + ' ' + fname.get() + ' ' + lname.get() + ' ' + password.get()
        msg = str(msg)
        makesure = msg.split()
        if len(makesure) == 4:
            b = msg.encode("utf-16")
            conn.send(b)
            b = conn.recv(1024)
            msg = b.decode('utf-16')
            if msg == 'AccountCreated':
                loginscreen()

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

#gör en klass för resor med de flesta nödvändiga attribut.
class Resa:
    def __init__(self, fromcity, tocity, time, month, date, klass, price):
        self.fromcity = fromcity
        self.tocity = tocity
        self.time = time
        self.month = month
        self.date = date
        self.klass = klass
        self.price = price

    def Generate(self , fromcity , tocity , time , month , date , klass , price):

        ticket = tk.Frame(rFrame , bg = 'white' , height = 200 , width = 640)
        ticket.pack(pady = 8 , padx = 6)

        destination = tk.Label(ticket , text = (fromcity + ' - ' + tocity) , bg = 'white')
        destination.config(font=('Helvatical bold',25))
        destination.place(x = 10 , y = 10 , anchor = tk.NW)

        departure = tk.Label(ticket , bg = 'white' , text = date + ':e ' + month + ' kl ' + time , fg = 'grey')
        departure.config(font=('Helvatical bold',20))
        departure.place(x = 630 , y = 12 , anchor = tk.NE)

        pricetext = tk.Label(ticket , bg = 'white' , text = price)
        pricetext.config(font=('Helvatical bold',22))
        pricetext.place(x = 10 , y = 165 , anchor = tk.SW)

        classtext = tk.Label(ticket , bg = 'white' , text = klass , fg = 'grey')
        classtext.config(font=('Helvatical bold',18))
        classtext.place(x = 10 , y = 165 , anchor = tk.NW)

        #speciell import för att kunna använda argument när en funktion hänvisas via tkinter knapp
        from functools import partial
        bookFunc = partial(Resa.book, self)

        #knapp för att boka resan
        bookB = tk.Button(ticket , bd = 2 , text = 'Boka!' , command = bookFunc , height = 2 , width = 8)
        bookB.config(font=('Helvatical bold',22))
        bookB.place(x = 610 , y = 160 , anchor = tk.SE)
    
    def book(self):
        msg = str(myID + ' ' + self.fromcity + ' ' + self.tocity + ' ' + self.time + ' ' + self.month + ' ' + self.date + ' ' + self.klass + ' ' + self.price)
        b = msg.encode('utf-16')
        conn.send(b)


def Search():
    #tar bort alla element i resultat framen, så att tickets inte stackas på varandra
    for widgets in rFrame.winfo_children():
        if widgets == Scroll:
            pass
        else:
            widgets.destroy()

    resorList = []

    #Hämtar information från alla filter
    for i in range(1,12):
        fromlist = []
        fromlist.append(FromStockholm.get())
        fromlist.append(FromMadrid.get())
        fromlist.append(FromParis.get())
        fromlist.append(FromDubai.get())
        fromlist.append(FromNewYork.get())
        fromlist.append(FromTokyo.get())

        tolist = []
        tolist.append(ToStockholm.get())
        tolist.append(ToMadrid.get())
        tolist.append(ToParis.get())
        tolist.append(ToDubai.get())
        tolist.append(ToNewYork.get())
        tolist.append(ToTokyo.get())

        classlist = []
        classlist.append(economy.get())
        classlist.append(plus.get())
        classlist.append(bussines.get())

        #fördeklaration av nödvändiga listor
        cities = ['Stockholm' , 'Madrid' , 'Paris' , 'Dubai' , 'NewYork' , 'Tokyo']
        classes = ['EconomyClass' , 'Plus' , 'BussinesClass']
        frominput = []
        toinput = []
        classinput = []

        #skriver om filterlistornas information från binär information till tillgänglig text.
        for i in range(0,5):
            if fromlist[i] == 0:
                pass
            else:
                frominput.append(cities[i])
            
            if tolist[i] == 0:
                pass
            else:
                toinput.append(cities[i])

        for i in range(0,2):
            if classlist[i] == 0:
                pass
            else:
                classinput.append(classes[i])
        
        #Visar allt om filter ej är aktiverade(används inte)
        if len(frominput) == 0:
            frominput = ['Stockholm' , 'Madrid' , 'Paris' , 'Dubai' , 'NewYork' , 'Tokyo']
        if len(toinput) == 0:
            toinput = ['Stockholm' , 'Madrid' , 'Paris' , 'Dubai' , 'NewYork' , 'Tokyo']
        if len(classinput) == 0:
            classinput = ['EconomyClass' , 'Plus' , 'BussinesClass']

        #deklarerar element för objekt generation
        fromcityi = str(frominput[r.randint(0,(len(frominput))-1)])
        tocityi = str(toinput[r.randint(0,(len(toinput))-1)])     
        timei = str(r.randint(10,23)) + ':' + str(r.randint(10,59))
        monthi = str(months[date-1])
        datei = str(r.randint(3,28))
        klassi = str(classinput[r.randint(0,(len(classinput)-1))])
        if klassi == 'Economy class':
            pricei = str(r.randint(900,1500)) + 'kr'
        elif klassi == 'Plus':
            pricei = str(r.randint(1600,2200)) + 'kr'
        else:
            pricei = str(r.randint(2400,4000)) + 'kr'
        
        #genererar objektet
        if fromcityi == tocityi:
            pass
        else:
            resorList.append(Resa(fromcityi , tocityi , timei , monthi , datei , klassi , pricei))

    #kallar till biljett genereringen
    for obj in resorList:
        obj.Generate(obj.fromcity , obj.tocity , obj.time , obj.month , obj.date , obj.klass , obj.price)


#beskrivning
def shop():
    pass


def profile():
    if myID == 10:
        pass
    else:
        pass


#deklarerar elementen för login screenen    
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
mButton = tk.Button(mFrame , image = adalaLogo2 , bd = 0 , bg = 'orange' , activebackground = 'orange' , command = shop)
pButton = tk.Button(mFrame , image = profileimg , bg = 'orange' , bd = 0 , activebackground = 'orange' , command = profile)


#deklarerar elementen för "biljettklass rutan"
cFrame = tk.Frame(c , bg = 'white' , bd = 0 , height = 80 , width = 669)

searchB = tk.Button(cFrame , bg = 'white' , activebackground = 'white' , bd = 0 , image = searchimg , command = Search)

economy = tk.IntVar()
plus = tk.IntVar()
bussines = tk.IntVar()

economyB = tk.Checkbutton(cFrame , variable = economy , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0 , text = 'Economy')
plusB = tk.Checkbutton(cFrame , variable = plus , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0 , text = 'Plus')
bussinesB = tk.Checkbutton(cFrame , variable = bussines , onvalue = 1 , offvalue = 0 , bg = 'white' , bd = 0 , text = 'Bussines')


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
fFrame = tk.Frame(c , bg = 'white' , bd = 0 , height = 545 , width = 300)

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
ScrollFrame = tk.Canvas(bg = 'lightgrey' , bd = 0 , height = 460 , width = 665)
rFrame = tk.Canvas(bg = 'lightgrey' , bd = 0 , height = 460 , width = 660)
ScrollFrame.pack_propagate(0)
Scroll = tk.Scrollbar(ScrollFrame , orient = 'vertical')
rFrame.config(yscrollcommand=Scroll.set)
Scroll.config(command=rFrame.yview)


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


#innehåller allt som ska ske i loopen, alltså ritas var 17:e sekund. funktionen är endast aktiv under inloggnings skärmen.
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
    ScrollFrame.place(anchor = tk.NW , x = 0 , y = 140)
    Scroll.pack(side = tk.RIGHT , fill = tk.Y)

    Search()


#startar loopen
loop()


#markerar slutet för tk-fönstret
c.mainloop()