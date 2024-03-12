def ot(gy :int, d :int, v:int):
    print('\n5. feladat')
    if gy > d + v:
        print('A csapatnak több győztes mérkőzése volt, mint veresége és döntelene együttvéve.')
    else:
        print('A csapatnak nem volt több győztes mérközése, mint veresége és döntelene együttvéve.')

def hat(fordsz :int, golk):
    print('\n6. feladat')
    sikerult = 0
    for index in range(fordsz-1):
        if 0 < golk[index]< golk[index + 1]: #0 < golkulonbsegek[index] and golkulonbsegek[index] < golkulonbsegek[index + 1]: 
            sikerult += 1
    if sikerult:
        print(f'A kitűzött célt {sikerult} alkalommal sikerült elérnie a csapatnak.')
    else:
        print('A kitűzött célt sajnos egyetlen alaklommal sem sikerült elérnie a csapatnak.')