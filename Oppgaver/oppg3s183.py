maned=int(input('Skriv inn tallet på måneden: '))

if maned>=1 and maned<=12:
    print('Gyldig måned.')
    if  maned<=3:
        print ('Første kvartal')
    else:
        if maned<=6:
            print('Andre kvartal')
        else:
            if maned<=9:
                print('Tredje kvartal')
            else:
                if maned<=12:
                    print ('Fjerde kvartal')

else:
    print ('Ugyldig måned.')
