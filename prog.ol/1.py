runvar = True
while runvar == True:
    try:
        Ku = int(input('Kuvert ? '))
        Af = int(input('Affisch ? '))
        Bl = int(input('Blad ? '))
        if 50 < Ku < 200 and 50 < Af < 200 and 50 < Bl < 200:
            runvar = False
        else:
            print('Vänligen ange endast heltal mellan 50 & 200')
    except:
        print('Vänligen ange endast heltal mellan 50 & 200')
svar = (Ku / 10**6) * 229 * 324 * 2 + (Af / 10**6) * 297 * 420 + (Af / 10**6) * 297 * 420 + (Bl / 10**6) * 210 * 297
print(f'Svar: {svar}')