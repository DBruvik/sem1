import os

nyHund='j'
print('Du har valgt 1, registrering av hund.')
print()
while nyHund=='j' or nyHund=='J':
    hundEksisterer=False
    while hundEksisterer==False:
        
        hundidnr=input('Skriv inn hundeID eller n/N for å gå tilbake til hovedmeny: ')
           
        hundidfil=open('hundregister.txt','r')
        soket=hundidfil.readline()
        #Testing på avslutte delprogram
        if hundidnr=='n' or hundidnr=='N':
            nyHund=0
            hundEksisterer=True
            soket=''
            print()
            print('Tilbake til hovedmeny')
            print()
        #Søker etter student
        while soket!='':
            soket=soket.rstrip('\n')

            if soket==hundidnr:
                print('Hunde nummer',hundidnr,'finnes allerede i registret og lagres ikke.')
                hundEksisterer=True
            soket=hundidfil.readline()
        
        hundidfil.close()
        #Studentnr eksisterer ikke i student.txt
        if not hundEksisterer:
            kundeEksisterer=False
            while kundeEksisterer==False:
                
                mobilnr=input('Skriv inn mobilnummer på kunde eller n/N for å gå tilbake til hovedmeny: ')
                   
                kunderegisterfil=open('kunderegister.txt','r')
                soket=kunderegisterfil.readline()
                #Testing på avslutte delprogram
                if mobilnr=='n' or mobilnr=='N':
                    nyKunde=0
                    kundenEksisterer=''
                    soket=''
                    print()
                    print('Tilbake til hovedmeny')
                    print()
                #Søker etter student
                while soket!='':
                    soket=soket.rstrip('\n')

                    if soket==mobilnr:
                        print('Kundemobilnummer',mobilnr,'finnes allerede i registret hund kan lagers.')
                        kundeEksisterer=True
                    soket=kunderegisterfil.readline()
                
            kunderegisterfil.close()
            #START HUND APPEND
            if kundeEksisterer==True and hundEksisterer==False:
                hundidfil=open('hundregister.txt','a')
                print('Registrerer hund ID', hundidnr)
                hundnavn=input('Skriv inn navn på hund: ')
                rase=input('Skriv inn rase på hund: ')
                startdato=input('Skriv inn dato for opphold: ')

                #Skriver inn studentopplysningene
                hundidfil.write(hundidnr+'\n')
                hundidfil.write(hundnavn+'\n')
                hundidfil.write(rase+'\n')
                hundidfil.write(mobilnr+'\n')
                hundidfil.write(startdato+'\n')
                print('Hunden er nå lagret!')
                #Studentopplysningene er lagt til i student.txt og spør om du vil legge til fler
                hundidfil.close()
                print('j/J for å legge til ny kunde eller n/N for å gå til hovedmeny')
                nyKunde=input('Vil starte på nytt? ')

print('Daniel')
