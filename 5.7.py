
def generatorZakresu(start,stop,krok = 1):
    start-=krok
    stop-=krok
    while start<stop:
        start +=krok
        yield start

for x in generatorZakresu(0,10,3):  # Nasza funkcja range
    print(x)

for y in range(0,10,3):      # Porownanie wynikow z naszym generatorem
    print(y)



