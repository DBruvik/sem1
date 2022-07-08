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
