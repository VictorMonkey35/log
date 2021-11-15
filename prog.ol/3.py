runvar = True
while runvar == True:
    try:
        N = int(input('Antal med grönt kort, N  ? '))
        M = int(input('Antal utan grönt kort, M ? '))
        if 2 <= N <= 400000000 and 0 <= M <= 400000000:
            runvar = False
        else: print('Kontrollera så att de angivna värderna är tillåtna.')
    except:
        print('Kontrollera så att de angivna värderna är tillåtna.')

if M < N:
    tid = 0
    tidvar = True
    while tidvar == True:
        if M <= 0:
            tid += 20
            tidvar = False
        else:
            tid += 10
            M -= M
            N -= (N - (N-M))/2
            N -= M
            
else:
    tid = 0
    tidvar = True
    while tidvar == True:
        if M > N:
            tid += 10
            M -= N
        else:
            tidvar = True
            while tidvar == True:
                if M <= 0:
                    tid += 20
                    tidvar = False
                else:
                    tid += 10
                    M -= M
                    N -= (N - (N-M))/2
                    N -= M
        
    

print(f'Svar: {tid}')