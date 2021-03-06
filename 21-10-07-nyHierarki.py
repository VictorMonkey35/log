class familj:
    def __init__(self, efternamn, roll):
        self.efternamn = efternamn
        self.roll = roll

class medlemm(familj):
    def __init__(self, efternamn, roll, namn):
        super().__init__(efternamn, roll)
        self.namn = namn

class husdjur(medlemm):
    def __init__(self, efternamn, roll, namn, art):
        super().__init__(efternamn, roll, namn)
        self.art = art

class person(medlemm):
    def __init__(self, efternamn, roll, namn, ålder):
        super().__init__(efternamn, roll, namn)
        self.ålder = ålder

jag = person('Forsebäck', 'son', 'victor', 18)
katt = husdjur('Forsebäck', 'djur', 'dog', 3)