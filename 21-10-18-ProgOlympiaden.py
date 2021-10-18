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
            print(f'''Du har {r} antal rader och {lamps} stycken lampor.
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
    if 0 <= i <= r:
        #append uppe
    elif r <= i <= r*2:
        #append höger
    elif r*2 <= i <= r*3:
        #append nere
    else r*3 <= i <= r*4:
        #append vänster


print(lampor)