#Program for å finne minste tall og tallnummer i en tallrekke på 5 tall
#Ønsker å plukke ut første gang tallet forekommer ved samme tall flere ganger

minsteTall=1000
tallnr=0

for n in range(1,6,1):
    print('Tall nr:',n)
    tall=int(input('Oppgi tall: '))
    if tall<minsteTall:
        minsteTall=tall
        tallnr=n
    else:
        if tallnr==0:
            minsteTall=tall
            tallnr=1
    print()

print('Minste tall er',minsteTall,'og det er tall nr',tallnr,'i rekka')
