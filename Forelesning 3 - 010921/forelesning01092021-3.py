#Beregning av bruttolønn, skattetrekk og netto utbetalt

#Først trenger vi inndata fra brukeren

timelonn=float(input('Skriv inn timelønn: '))
antallTimer=float(input('Skriv inn arbeidstimer: '))

#Beregne bruttolønn
bruttolonn=timelonn*antallTimer

#Finne riktig skattesats
if bruttolonn<20000:
    skattesats=28
else:
    skattesats=35
    if bruttolonn<30000:
        skattesats=35
    else:
        skattesats=40

#Beregner skatt og nettolønn
skattIKr=bruttolonn*skattesats/100
nettolonn=bruttolonn-skattIKr

#Skriv ut lønnsberegningen
print ('Din bruttolønn er da', format(bruttolonn,'.2f'))
print('Din skatteprosent er',skattesats,'og skattetrekket i kr er', format(skattIKr,'.2f'))
print('Du får utbetalt',format(nettolonn,'.2f'),'kr')

