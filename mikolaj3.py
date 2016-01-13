import random
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

class Mikolaj(IstotaRuchoma, IstotaSpelniajacaZyczenia):
    _liczbaMikolajow = 0
    def __init__(self):
        #self.__class__._liczbaMikolajow+=1   //  Mozna tak lub tak jak nizej
        Mikolaj._liczbaMikolajow +=1

        return

    def podarujPrezent(self,imieDziecka):
        self.spelnijZyczenie(imieDziecka.nazwa)


#--------------------------------------------------------

class RobotJednorozec(IstotaSpelniajacaZyczenia):
    _zyczeniaDoSpelnienia = 0

    def __init__(self):
        return

#--------------------------------------------------------

class beczka():
    def __init__(self):
        return

#--------------------------------------------------------

lista = []

for i in range(0,10):
    i = Mikolaj()
    lista.append(i)

for i in range(10,15):
    i = RobotJednorozec()
    lista.append(i)

for i in range(15,17):
    i = beczka()
    lista.append(i)

random.shuffle(lista)

print(lista)
ile = 0
for i in lista: # mozna by dodac do kazdego issubclass()
    ile +=1
    print('Obiekt nr {} dokladnie - > {}'.format(ile,i))
    if isinstance(i,IstotaRuchoma):
        i._maxV += 1
        print('maxV --')
    if isinstance(i,Byt):
        i._energia /= 2
        print('energa /2')
    if isinstance(i,RobotJednorozec):
        i._zyczeniaDoSpelnienia += 3
        print('zyczenia +=3')
    if isinstance(i,beczka):
        print('Bumm !!')
print('Liczba Mikolajow = {}'.format(Mikolaj._liczbaMikolajow))