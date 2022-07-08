import os

nyHund='j'
print('Du har valgt 1, registrering av hund.')
print()
while nyHund=='j' or nyHund=='J':
    hundEksisterer=False
    while hundEksisterer==False:

        hundidnr=input('Skriv inn hundeID eller n/N for å gå tilbake til hovedmeny: ')
           
        hundidfil=open('hundregister.txt','r')
        hundRegisterHundid=hundidfil.readline().rstrip('\n')
        #Testing på avslutte delprogram
        if hundidnr=='n' or hundidnr=='N':
            nyHund=0
            hundEksisterer=''
            soket=''
            print()
            print('Tilbake til hovedmeny')
            print()

        while hundRegisterHundid!='':
            hundRegisterHundNavn=hundidfil.readline().rstrip('\n')
            hundRegisterHundRase=hundidfil.readline().rstrip('\n')
            hundRegisterHundMobil=hundidfil.readline().rstrip('\n')
            hundRegisterHundStartdato=hundidfil.readline().rstrip('\n')

            if hundRegisterHundid==hundidnr:
                hundEksisterer=True
            hundRegisterHundid=hundidfil.readline().rstrip('\n')
        hundidfil.close()

        if hundEksisterer==False:
            kundeEksisterer=False

            mobilnr=input('Skriv inn mobilnummer eller n/N for å gå tilbake til hovedmeny: ')
        
            kundefil=open('kunderegister.txt','r')
            kundeRegisterMobil=kundefil.readline().rstrip('\n')

            while kundeRegisterMobil!='':
                kundeRegisterFornavn=kundefil.readline().rstrip('\n')
                kundeRegisterEtternavn=kundefil.readline().rstrip('\n')
                kundeRegisterKort=kundefil.readline().rstrip('\n')

                if kundeRegisterMobil==mobilnr:
                    kundeEksisterer=True

                kundeRegisterMobil=kundefil.readline().rstrip('\n')

            kundefil.close()

            if kundeEksisterer==True and hundEksisterer==False:
                hundidfil=open('hundregister.txt','a')
                print('Kunde finnes i systemet, fortsetter med hunde opplysninger.')
                hundNavn=input('Navn på hund: ')
                hundRase=input('Rase på hund: ')
                hundDato=input('Dato for hund: ')

                hundidfil.write(hundidnr+'\n')
                hundidfil.write(hundNavn+'\n')
                hundidfil.write(hundRase+'\n')
                hundidfil.write(mobilnr+'\n')
                hundidfil.write(hundDato+'\n')
                print('Hund er lagret')

                hundidfil.close()

            else:
                print('Kunde eksisterer ikke og hund kan ikke registreres.')
        else:
            if hundidnr=='n' or hundidnr=='N':
                print('Avslutter')
            else:
                print('Denne hunden er allerede registrert.')
print('Daniel')
