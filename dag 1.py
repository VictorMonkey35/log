import math

print('Talen A & B bör endast vara produkter av upphöjt till 10.')
print('Ange A:')
A = int(input())
print('Ange + eller *')
op = str(input())
print('Ange B:')
B = int(input())

def ask():
    print('Talen A & B bör endast vara produkter av upphöjt till 10.')
    print('Ange A:')
    A = int(input())
    print('Ange + eller *')
    op = str(input())
    print('Ange B:')
    B = int(input())

def check():
    if math.log(A) == int(math.log(A)):
        print('godkänt')
    else:
        print('icke godkänt tal A')
        print(A)
        print(math.log(A))

def calculate():
    if op == '*':
        result = A * B
    elif op == '+':
        result = A + B
    else:
        print('Vänligen ange ett godkänt räkne sätt.')

    print(f'ditt resultat är {result}.')

#för att checka nummret, logga och se till att det blir ett heltal.