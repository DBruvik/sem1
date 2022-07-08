fornavn=[]
nyttNavn='ja'

while nyttNavn == 'Ja' or nyttNavn == 'ja':
    navnListe=str(input('Skriv inn fornavn: '))
    nyttNavn=str(input('Vil du skrive inn nytt navn?Ja eller Nei.'))
    fornavn+=[navnListe]
    print('Fornavn til nå: ',fornavn)
