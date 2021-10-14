class Djur:
    def ät(self):
        print('Monch sounds.')
    def sov(self):
        print('ZZZ')

class Fisk(Djur):
    def __init__(self, name):
        self.name = name
    def simma(self):
        print('Fisken simmade iväg.')

class Haj(Djur):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def ät(self, name):
        print(f'{self.name} åt upp {name}.')

fishe = Fisk('Albin')
fishe.ät()
fishe.sov()

shork = Haj('Harald')

shork.ät(fishe.name)
shork.sov()

