import os

os.system('cls')

AskN = False
while AskN == False:
    try:
        global N

        print('''vänligen ange antalet skivor.
(Heltal mellan 1 & 12)''')
        N = int(input('->'))

        if N < 0:
            print('Vänligen ange ett heltal mellan 1 & 12')
        
        elif N > 12:
            print('Vänligen ange ett heltal mellan 1 & 12')
        
        else:
            AskN = True

    except:
        print('Vänligen ange ett heltal mellan 1 & 12')

AskM = False
while AskM == False:
    try:
        global M

        print('''vänligen ange antalet segment per skiva.
(Heltal mellan 1 & 12)''')
        M = int(input('->'))

        if M < 0:
            print('Vänligen ange ett heltal mellan 1 & 12')
        
        elif M > 12:
            print('Vänligen ange ett heltal mellan 1 & 12')
        
        else:
            AskM = True

    except:
        print('Vänligen ange ett heltal mellan 1 & 12')

komb = M**N

print('Ditt lås kan ha ' + str(komb) + ' Olika kombinationer')