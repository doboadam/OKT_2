from feladat4 import negy
from feladat5 import ot

def harom(golk):
    print('\n3. feladat')
    gyozelmek = 0
    veresegek = 0
    dontelenek = 0
    for golkulonbseg in golk:
        if golkulonbseg > 0:
            gyozelmek = gyozelmek + 1
        elif golkulonbseg < 0:
            veresegek = veresegek + 1
        else:
            dontelenek = dontelenek + 1
    print('A szezonban a csapatnak',gyozelmek, 'győzelme,', veresegek, 'veresége', dontelenek, 'döntetlene volt.')

    negy(gyozelmek, dontelenek)
    ot(gyozelmek, dontelenek,veresegek)
