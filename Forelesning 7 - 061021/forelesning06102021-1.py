#Program for å finne minste tall og tallnummer i en tallrekke på 5 tall


#For å unngå å bruke dummy lar en første tall en tar imot også være minstetall til nå
#Det gjør en i tilfelle utenfor for-løkka
#Ønsker å plukke ut første gang tallet forekommer ved samme tall flere ganger

print('Tall nr: 1')
tall=int(input('Oppgi tall: '))
minsteTall=tall
tallnr=1
print()

for n in range(2,6,1):
    print('Tall nr:',n)
    tall=int(input('Oppgi tall: '))
    if tall<minsteTall:
        minsteTall=tall
        tallnr=n
    print()

print('Minste tall er',minsteTall,'og det er tall nr',tallnr,'i rekka')
