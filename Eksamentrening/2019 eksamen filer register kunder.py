import os

nyKunde='j'
print('Du har valgt 1, registrering av studentnummer.')
print()
while nyKunde=='j' or nyKunde=='J':
    kundeEksisterer=False
    while kundeEksisterer==False:
        
        mobilnr=input('Skriv inn mobilnummer på kunde eller n/N for å gå tilbake til hovedmeny: ')
           
        kunderegisterfil=open('kunderegister.txt','r')
        soket=kunderegisterfil.readline()
        #Testing på avslutte delprogram
        if mobilnr=='n' or mobilnr=='N':
            nyKunde=0
            kundenEksisterer=True
            soket=''
            print()
            print('Tilbake til hovedmeny')
            print()
        #Søker etter student
        while soket!='':
            soket=soket.rstrip('\n')

            if soket==mobilnr:
                print('Kunde nummer',mobilnr,'finnes allerede i registret og lagres ikke.')
                kundeEksisterer=True
            soket=kunderegisterfil.readline()
        
        kunderegisterfil.close()
        #Studentnr eksisterer ikke i student.txt
        if not kundeEksisterer:
            kunderegisterfil=open('kunderegister.txt','a')
            print('Registrerer', mobilnr)
            fornavn=input('Skriv inn fornavn på kunde: ')
            etternavn=input('Skriv inn etternavn på kunde: ')
            kort=input('Skriv inn kort på kunde: ')

            #Skriver inn studentopplysningene
            kunderegisterfil.write(mobilnr+'\n')
            kunderegisterfil.write(fornavn+'\n')
            kunderegisterfil.write(etternavn+'\n')
            kunderegisterfil.write(kort+'\n')
            print('Kunden er nå lagret!')
            kundeEksisterer=True
            #Studentopplysningene er lagt til i student.txt og spør om du vil legge til fler
            kunderegisterfil.close()
            print('j/J for å legge til ny kunde eller n/N for å gå til hovedmeny')
            nyKunde=input('Vil du legge til flere kunder? ')

print('Daniel')
