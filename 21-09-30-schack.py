# https://open.kattis.com/problems/bijele

import os
import time as t
runVar = True
while runVar == True:
    try:
        os.system('cls')
        print('vänligen ange sättets skick')
        a = input('->')
        list = a.split()

        result = ''

        for i in range(6):
            if i == 0 or i == 1:
                result += str(1-int(list[i]))
            if i == 2 or i == 3 or i == 4:
                result += str(2-int(list[i]))
            if i == 5:
                result += str(8-int(list[i]))
            result += ' '
        print(result)
        runVar = False

    except:
        os.system('cls')
        print('vänligen ange sättets skick')
        print(f'->{str(a)}')
        print('')
        print('Något gick fel, vänligen ange 6 heltal med mellanrum.')
        print('.')
        t.sleep(1)
        os.system('cls')
        print('vänligen ange sättets skick')
        print(f'->{str(a)}')
        print('')
        print('Något gick fel, vänligen ange 6 heltal med mellanrum.')
        print('..')
        t.sleep(1)
        os.system('cls')
        print('vänligen ange sättets skick')
        print(f'->{str(a)}')
        print('')
        print('Något gick fel, vänligen ange 6 heltal med mellanrum.')
        print('...')
        t.sleep(1)
        os.system('cls')
        print('vänligen ange sättets skick')
        print(f'->{str(a)}')
        print('')
        print('Något gick fel, vänligen ange 6 heltal med mellanrum.')
        print('....')
        t.sleep(1)