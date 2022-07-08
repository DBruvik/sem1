#Program for å finne minste tall og tallnummer i en tallrekke på 5 tall

minsteTall=1000000000
tallnr=0

for n in range(1,6,1):
    print('Tall nr:',n)
    tall=int(input('Oppgi tall: '))
    if tall<=minsteTall:
        minsteTall=tall
        tallnr=n
    print()

print('Minste tall er',minsteTall,'og det er tall nr',tallnr,'i rekka')
