import random as r

class djur:
    def __init__(self, antalBen):
        self.antalBen = antalBen
    def visaben(self):
        print(f'Denna varelse har {self.antalBen} stycken ben')
    def dö(self):
        print('varelsen dog')

class människa(djur):
    def __init__(self, antalBen, namn):
        super().__init__(antalBen)
        self.namn = namn
    def visanamn(self):
        print(f'Denna varelse heter {self.namn}')
    def dö(self):
        print(f'{self.namn} dog')

rufus = människa(2, 'rufus')

dog = djur(5)

rufus.visanamn()
rufus.visaben()
rufus.dö()

dog.visaben()
dog.dö()