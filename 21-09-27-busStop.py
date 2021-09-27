import os

os.system('cls')

runvar = False

while runvar == False:
    try:
        AntalStopp = int(input('''ange antal buss stop
(ange ett heltal mellan 1 och 30.)
->'''))
        if AntalStopp < 1:
            print('ange ett heltal mellan 1 och 30')
        elif AntalStopp > 30:
            print('ange ett heltal mellan 1 och 30')
        else:
            runvar = True
    except:
        print('ange ett heltal mellan 1 och 30')

resultat = 0

def ettStop():
    global resultat
    resultat += 0.5
    resultat = 2 * resultat
    resultat = int(resultat)

for i in range(AntalStopp):
    ettStop()


print(f'Det var {resultat} stycken passagerare då bussen startade')