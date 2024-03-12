def ketto(max :int):
    import random
    print('\n2. feladat')
    golkulonbsegek = []
    for i in range(0, max):
        aktualis_ertek = random.randint(-3,4)
        golkulonbsegek.append(aktualis_ertek)
    return golkulonbsegek

