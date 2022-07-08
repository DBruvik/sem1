#Inndata test i begynnelsen av programmet

#Variabel til bruk til inndatatest, bols variabel
nyttTall=True

#Løkke som sikrer oss gyldig verdi
while nyttTall==True:
    #Brukeren oppgir verdi på ruletten
    tall=int(input('Hva er tallet på ruletten?'))

    #Tester om gyldig verdi
    if tall>=0 and tall<=36:
        print('Gyldig verdi')
        nyttTall=False
    else:
        print('Ugyldig verdi på ruletten, skriv inn nytt tall.')

print('Da har vi fått et gyldig tall på ruletten og kan fortsette programmet med å avgjøre riktig farge.')
