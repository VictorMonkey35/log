runvar = True
while runvar == True:
    try:
        ord = int(input('Antal ord ? '))
        if 1 <= ord <= 5:
            string = input('Mening ? ')

            count = 0
                
            for i in range(0, len(string)):
                    
                if string[i] == " ":
                    count += 1

            if (ord - 1) == count:
                runvar = False
            else:
                print('Det verkar som att meningen har fler ord än angivet, vänligen försök igen.')

    except:
        print('vänligen ange antal ord som ett heltal mellan 1 & 5')

kons = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z'}
vok = {'a','e','i','o','u','y'}

for i in range(0,(len(string)-3)):
    vari = string[i] in vok
    vari1 = string[i+1] in kons
    vari2 = string[i+1] in kons
    if vari == True:
        if vari1 == True and vari2 == True:
            string = string[0 : i : ] + string[i + 1 : :]
        else:
            pass
    else:
        pass

print(string[len(string)::-1])