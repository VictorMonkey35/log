import os

run = 'r'

while run != 'q':
    os.system('cls')

    print('Ange trollkarens magiska tal.')

    verify = True

    while verify:
        try:
            x = int(input('-> '))
            if x < 0:
                print('Vänligen ange ett heltal mellan 0 och 100')
            elif x > 100:
                print('Vänligen ange ett heltal mellan 0 och 100')
            else:
                verify = False
        except:
            print('Vänligen ange ett heltal mellan 0 och 100')

    for i in range (1,x+1):
        print(i,'Abracadabra')


    print('vill du köra igen? ( "q" för att avsluta)')
    runID = input('->')

    if runID == 'q':
        quit()
    else:
        pass

    
