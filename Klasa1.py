class ulamek:
    
    def __init__(self,licznik,mianownik):
        self._licznik = int(licznik)
        self._mianownik = int(mianownik)
        
    def wypisz(self):
        print("{} / {} = {}".format(self._licznik,self._mianownik,self._licznik/self._mianownik))

    def mnozenie(self,obiekt):
        return print("{} / {} = {}".format(self._licznik*obiekt._licznik,self._mianownik*obiekt._mianownik,
                                           (self._licznik*obiekt._licznik)/(self._mianownik*obiekt._mianownik)))


class superUlamek(ulamek):
    
    def gcd(self):
        a=self._licznik
        b=self._mianownik
        while b != 0:
            (a,b)=(b, a % b)
        return abs(a)

    def mnozenie(self,obiekt):
        super(superUlamek,self).mnozenie(obiekt)

    def uprosc(self):
        x=self.gcd()
        self._licznik = self._licznik/x
        self._mianownik = self._mianownik/x

x4 = superUlamek(42,56)
print ('przed')
x4.wypisz()

print('po')
x4.uprosc()
x4.wypisz()



