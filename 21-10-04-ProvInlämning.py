import os
os.system('cls')
lista = []

askRader = True
while askRader == True:
    try:
        print('Ange antal rader.')
        rader = int(input('->'))
        if rader < 1:
            print('antalet rader bör vara ett heltal mellan 1 och 5')
        elif rader > 5:
            print('antalet rader bör vara ett heltal mellan 1 och 5')
        else:
            askRader = False
    except:
        print('antalet rader bör vara ett heltal mellan 1 och 5')

for i in range(1,rader+1):
    run = True
    while run == True:
        try:
            os.system('cls')
            print(f'Ange nummer {i}')
            x = int(input('->'))
            lista.append(x)
            run = False
        except:
            pass

lista.reverse()

os.system('cls')

for item in lista:
    print(item)