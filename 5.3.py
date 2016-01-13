import random
class choinka:
    def __init__(self,roz):
        self._rozmiar=roz
        self._ozdoby = ['@','#','$','%','*','&','+']
    def __str__(self):
        znak = 1
        biale = self._rozmiar - 1
        for i in range(0, self._rozmiar):

            for k in range(0,biale):
                print(' ',end='')
            biale= biale-1

            for j in range(0,znak):
                x=random.choice(self._ozdoby)
                print(x,end='')
            znak = znak+2
            print('')
        for l in range(0,self._rozmiar-2):
            print(' ',end='')
        print('| |')

drzewko1 = choinka(10)

#str(drzewko1) <-- powinno byc, ale wywala error,
#                   mimo ze wywoluej to co nizej wtf ?
#
drzewko1.__str__()





