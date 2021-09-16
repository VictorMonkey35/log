import os

os.system('cls')


def räknaUt():
    a = input('Vänligen ange dina tal: ').split()

    X = [int(x) for x in a]

    print('Din summa är:')

    print(sum(X))

räknaUt()