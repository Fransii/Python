
byty = {}

#-------------------------------------------------------

class Byt:
    _nazwa = 0
    _polozenie = 0,0
    _energia = 0
    def __init__(self,nazwa,polozenie,energia):
        self._nazwa = nazwa
        self._polozenie = polozenie
        self._energia = energia
        byty[self._nazwa] = self._polozenie

#-------------------------------------------------------

class IstotaRuchoma(Byt):
    _maxV = 0
    def __init__(self):
        return
    def idzDo(self,gdzie):
        #Jak zmienic polozenie?

        self._polozenie = gdzie
        self._energia = self._energia -1


#-------------------------------------------------------

class IstotaSpelniajacaZyczenia(Byt):
    def __init__(self):
        return
    def spelnijZyczenie(self,nazwa):
        self.idzDo(byty[nazwa])
        polozenie = byty[nazwa]
        if self._polozenie == polozenie:
            print('Zyczenie {}a spelnione! '.format(nazwa))
            self._energia = self._energia -1.5
            del byty[nazwa]
        else:
            print('Nie mozna spelnic zyczenia!')


#-------------------------------------------------------

class Milokaj(IstotaRuchoma,IstotaSpelniajacaZyczenia):
    def __init__(self,nazwa,polozenie,energia):
        self._nazwa = nazwa
        self._polozenie = polozenie
        self._energia = energia
    def podarujPrezent(self,imieDziecka):
        self.spelnijZyczenie(imieDziecka.nazwa)


#--------------------------------------------------------

dziecko1 = Byt('Andrzej',4,10)
dziecko2 = Byt('Janusz',6,15)
dziecko3 = Byt('Kamil',1,8)

print('Dzieci z zyczeniami:')
print(byty)
print()

mikolaj = Milokaj('Mikołaj',4,10)
mikolaj.spelnijZyczenie('Andrzej')
mikolaj.spelnijZyczenie('Janusz')
print('Dzieci z zyczeniami po wizycie Mikolaja:')
print(byty)
print()
print('Energia Mikolaja po rozdaniu prezentow: ')
print(mikolaj._energia)
print()



