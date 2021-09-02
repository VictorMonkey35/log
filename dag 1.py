import math

import os

verify = 0

A = 0

B = 0

op = "string"

run = "string"

def ask():

    global A
    global op
    global B

    print('Talen A & B bör endast vara produkter av upphöjt till 10.')
    
    print('Ange A:')
    askrun1 = True
    while askrun1:
        try:
            A = int(input())
            askrun1 = False
        except:
            print('vänligen ange ett heltal med potensialbasen 10')

    print('Ange + eller *')
    askrun2 = True
    while askrun2:
        try:
            op = str(input())
            askrun2 = False
        except:
            print('vänligen ange operationerna + eller *')

    print('Ange B:')
    askrun3 = True
    while askrun3:
        try:
            B = int(input())
            askrun3 = False
        except:
            print('vänligen ange ett heltal med potensialbasen 10')

def check():
    if math.log10(A) == int(math.log10(A)):
        global verify
        verify += 1
    else:
        print('icke godkänt tal A')
        print(A)

    if math.log10(B) == int(math.log10(B)):
        verify += 1
    else:
        print('icke godkänt tal B')
        print(B)

def calculate():
    if op == '*':
        result = A * B
    elif op == '+':
        result = A + B
    else:
        print('Vänligen ange ett godkänt räkne sätt.')

    print(f'ditt resultat är {result}.')

def end():
    print('''vill du fortsätta?
    (skriv "q" För att Avsluta.''')
    global run
    run = input('->')

    if run == 'q':
        global i
        i += 1
    
    else:
        pass



i = 1

while i == 1:
    os.system('cls')

    ask()

    check()

    if verify == 2:
        calculate()
    else:
        print('talen är ej valida.')

    end()
    

#för att checka nummret, logga och se till att det blir ett heltal.