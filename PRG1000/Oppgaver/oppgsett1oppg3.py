karakterA=92
karakterB=77
karakterC=58
karakterD=46
karakterE=40

karakter=int(input('Skriv inn din poengsum på prøven: '))
if karakter>=karakterA:
    print('Din karakter er A.')     
else:
    if karakter>=karakterB:
        print('Din karakter er B.')
    else:
        if karakter>=karakterC:
            print('Din karakter er C.')
        else:
            if karakter>=karakterD:
                print('Din karakter er D.')
            else:
                if karakter>=karakterE:
                    print('Din karakter er E.')
                else:
                    print ('Din karakter er F.')
