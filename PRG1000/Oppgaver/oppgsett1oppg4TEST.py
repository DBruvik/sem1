En=float(input('Skriv inn første tallet du tenker på: '))
To=float(input('Skriv inn andre tallet du tenker på: '))
Tre=float(input('Skriv inn tredje tallet du tenker på: '))
Fire=float(input('Skriv inn fjerde tallet du tenker på: '))
Fem=float(input('Skriv inn femte tallet du tenker på: '))

minListe=[En,To,Tre,Fire,Fem]
minListe=sorted(minListe, reverse=False)
print (minListe)
