tall=int(input('Skriv inn tallet du fikk: '))

if tall==0:
    print('Tallet er', tall,'og er alene på fargen grønn.')
if tall >0 and tall <=10 and (tall%2)==0:
    print('Tallet er', tall,'og er i intervallet [1,10].')
    print('Tallet ditt er partall.')
if tall >0 and tall <=10 and (tall%2)!=0:
    print('Tallet er', tall,'og er i intervallet [1,10].')
    print('Tallet ditt er Oddetall.')
if tall >10 and tall <=18 and (tall%2)==0:
    print('Tallet er', tall,'og er i intervallet [11,18.]')
    print('Tallet ditt er partall.')
if tall >10 and tall <=18 and (tall%2)!=0:
    print('Tallet er', tall,'og er i intervallet [11,18].')
    print('Tallet ditt er Oddetall.')
if tall >18 and tall <=28 and (tall%2)==0:
    print('Tallet er', tall,'og er i intervallet [19,28].')
    print('Tallet ditt er partall.')
if tall >18 and tall <=28 and (tall%2)!=0:
    print('Tallet er', tall,'og er i intervallet [19,28].')
    print('Tallet ditt er Oddetall.')
if tall >28 and tall <=36 and (tall%2)==0:
    print('Tallet er', tall,'og er i intervallet [29,36].')
    print('Tallet ditt er partall.')
if tall >28 and tall <=36 and (tall%2)!=0:
    print('Tallet er', tall,'og er i intervallet [29,36].')
    print('Tallet ditt er Oddetall.')

#Ståle: >=1, >=11 osv, over >0. Han hadde også med fargen på ruletten
#Låse tallene fra 0-36
#if tall==0: > else: > uavhengige if > Else ugyldig tall(må ikke være med)
