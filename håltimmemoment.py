import os

resultat = []

boys = 0

run = '1'

def lägTill():
    global resultat
    global boys
    runvar = False
    while runvar == False:
        try:
            boys = int(input('hur många människor finns i rummet? '))
            runvar = True
        except:
            print('vänligen ange ett heltal')

    for i in range (boys):
        verify = False
        while verify == False:
            try:
                appendvar = input('skriv in resultatet: ')
                resultat.append(appendvar)
                verify = True
            except:
                print('vänligen ange ett heltal')

        


def skriv():
    global resultat
    global boys
    global run
    for i in range (boys):
        print(resultat[0])
        resultat.pop(0)

while run == '1':
    os.system('cls')
    lägTill()
    print('vill du även dela ut prov?(Skriv "Ja" för att skriva ut.)')
    printvar = input('->')

    if printvar == 'Ja':
        skriv()
    else:
        pass

    run = (input('''Vill du fortsätta dela ut prov?
    (Skriv "1" för att fortsätta.)'''))


