import os
import random as r
import time as t
import math as m

os.system('cls')

class object:
    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY

class vector(object):
    def __init__(self, positionX, positionY, angle, length):
        super().__init__(positionX, positionY)
        self.angle = angle
        self.length = length

def makeBalls(positionX, positionY, angle, length):
    global vector1
    vector1 = vector(positionX, positionY, angle, length)
    dot = '.'
    for i in range(1,4):
        os.system('cls')
        print(f'calculating {dot * i}')
        t.sleep(0.6)

    print('Done!')
    t.sleep(0.4)
    os.system('cls')
    
runvar = True
while runvar == True:
    try:
        print('Please make vector.')
        print('position X:')
        posX1 = int(input('->'))
        os.system('cls')
        print('Please make vector.')
        print('positionY')
        posY1 = int(input('->'))
        os.system('cls')
        print('Please make vector.')
        print('angle')
        angle1 = int(input('->'))
        os.system('cls')
        length1 = m.sqrt(posX1**2 + posY1**2)
        runvar = False
    except:
        print('''something went wrong...
remember to only input integers.''')

makeBalls(posX1, posY1, angle1, length1)

print(f'Vector length is {vector1.length}.')
input()