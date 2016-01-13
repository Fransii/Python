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

class Milokaj(IstotaRuchoma,IstotaSpelniajacaZyczenia):
    def __init__(self):
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


mikolaj1 = Milokaj()
mikolaj2 = Milokaj()
mikolaj3 = Milokaj()
mikolaj4 = Milokaj()
mikolaj5 = Milokaj()

robot1 = RobotJednorozec()
robot2 = RobotJednorozec()
robot3 = RobotJednorozec()
robot4 = RobotJednorozec()
robot5 = RobotJednorozec()

beczka1 = beczka()
beczka2 = beczka()

lista = [mikolaj1,mikolaj2,mikolaj3,mikolaj4,mikolaj5,robot1,robot2,robot3,robot4,robot5,beczka1,beczka2]
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