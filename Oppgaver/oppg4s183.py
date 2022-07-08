tall=int(input('Skriv inn tallet du ønsker å vite: '))

if tall>=1 and tall<=10:
    print('Gyldig tall')
    if tall==1:
        print('Romersk symbol er: I')
    if tall==2:
        print('Romersk symbol er: II')
    if tall==3:
        print('Romersk symbol er: III')
    if tall==4:
        print('Romersk symbol er: IV')
    if tall==5:
        print('Romersk symbol er: V')
    if tall==6:
        print('Romersk symbol er: VI')
    if tall==7:
        print('Romersk symbol er: VII')
    if tall==8:
        print('Romersk symbol er: VIII')
    if tall==9:
        print('Romersk symbol er: IX')
    if tall==10:
        print('Romersk symbol er: X')
else:
    print('Romersk symbol er: Ugyldig tall')
