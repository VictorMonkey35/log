#översätt en mening till rövarspråket.

#A B C D E F G H I J K L M N O P Q R S T U V X Y Z Å Ä Ö
#  B C D   F G H   J K L M N   P Q R S T   V X   Z

dic = {'a': 'a', "b": "bob", "c": "coc", "d": "dod", 'e': 'e', "f": "fof", "g": "gog", "h": "hoh", 'i': 'i', "j": "joj", "k": "kok", "l": "lol", "m": 'mom', 'n': 'non', 'o': 'o', 'p': 'pop', 'q': 'qoq', 'r': 'ror', 's': 'sos', 't': 'tot', 'u': 'u', 'v': 'vov', 'x': 'xox', 'y': 'y', 'z': 'zoz', 'å': 'å', 'ä': 'ä', 'ö': 'ö'} 

ord = input('skriv ord ->')

ord = ord.lower()

sos = []

sos.append(ord)

print(sos)

#gör dic för alfabet
#gör input till lista
#gör funktion som gör varje bokstav,listobjekt, till sin dic verision.