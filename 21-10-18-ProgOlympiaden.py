import os
from typing import get_args
os.system('cls')

print('Ange antal kolumner/rader')
r = int(input('->'))

lamps = r*4

rutor = r**2

lampor = []

for i in range(1, lamps + 1):
    runvar = True
    while runvar == True:
        try:
            os.system('cls')
            print(f'''Du har {r} lampor per rad och {lamps} stycken lampor.
Lampa 1 är den vänstra i övre raden. Du går sedan medurs.
ange färgen för lampa {i}(rgb).''')
            x = input('->')
            if x == 'r' or x == 'g' or x == 'b':
                lampor.append(x)
                runvar = False
        except:
            print('fel.')

upp = []
höger = []
ned = []
vänster = []

for i in range(lamps):
    if 0 <= i <= r-1:
        upp.append(str(lampor[i]))
    elif r <= i <= (r*2)-1:
        höger.append(str(lampor[i]))
    elif r*2 <= i <= (r*3)-1:
        ned.append(str(lampor[i]))
    else:
        vänster.append(str(lampor[i]))

vitarutor = 0

for i in range(r):
    for j in range(r):
        colset = {}
        colset.add(upp[j])
        colset.add(ned[j - r])
        colset.add(vänster[i - r])
        colset.add(höger[i])
        if len(colset) == 3:
            vitarutor += 1
        else:
            pass

print(f'Rutnätet har {vitarutor} av {rutor} antal vita rutor.')