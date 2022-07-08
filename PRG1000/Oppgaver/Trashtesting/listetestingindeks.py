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
    
if talliste[0]>talliste[1]:
    minst=talliste[1]
    indeks=2
else:
    minst=talliste[0]
    indeks=1
if minst>talliste[2]:
    minst=talliste[2]
    indeks=3
if minst>talliste[3]:
    minst=talliste[3]
    indeks=4
if minst>talliste[4]:
    minst=talliste[4]
    indeks=5
    
#utskrift av listeinnhold og listestørrelse etter fylling
print('Hele lista er:',talliste)
listeLengde=len(talliste)

print('Minste tallet er',minst, 'og tall nr er',indeks)


print('Antall elementer i lista er: ',listeLengde)

#Prøv selv/oppgave til neste gang
#utvid programmet til å finne minste tall og tallnr i lista
