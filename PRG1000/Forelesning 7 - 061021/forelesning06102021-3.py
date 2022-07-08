#Program for å lese 5 tall inn i en liste og finne det minste tallet

#Talliste defineres som en tom liste
talliste=[]

#Utskift av listeinnhold før fylling
print('Lista til nå:', talliste)
print()

#for-løkke for å lese 5 tall inn i lista talliste
for indeks in range(0,5,1):
    print('Tall nr:',indeks+1)
    listeverdi=int(input('Oppgi tall: '))
    #Innlest listeverdi legges inn i lista
    talliste+=[listeverdi]
    #Utskrift av listeinnhold underveis/med fylling
    print('Lista til nå:', talliste)
    print()

#utskrift av listeinnhold og listestørrelse etter fylling
print('Hele lista er:',talliste)
listeLengde=len(talliste)

print('Antall elementer i lista er: ',listeLengde)

#Prøv selv/oppgave til neste gang
#utvid programmet til å finne minste tall og tallnr i lista

#Her starter utvidelse av program forelesninge22092021-4
#Klargjøring for å finne minste tall, settes til første tall i lista utenfor løkka
minsteTall=talliste[0]
tallnr=1

for indeks in range(1,5,1):
    if talliste[indeks]<minsteTall:
        #Da er det et nytt tall som er minstetall
        minsteTall=talliste[indeks]
        #Tall nr i rekka er indeks i lista pluss 1
        tallnr=indeks+1

print('Det minste tallet er ', minsteTall,'og det er tall nr',tallnr,'i lista')

