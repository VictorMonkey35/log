#https://open.kattis.com/problems/fyi

import os
os.system('cls')

runVar = True
while runVar == True:
    try:
        print('Please enter the correct number.')
        number = int(input('->'))
        if number < 1000000:
            print('The number has to contain seven digits only.')
        elif number > 9999999:
            print('The number has to contain seven digits only.')
        else:
            runVar = False
    except:
        print('The number has to contain 7 digits only.')

if (int(str(number)[:3])) == 555:
    print(1)
else:
    print(0)