#Oppgave 3 oppgavesett 1, med nøsta hvis-setninger, tester < og starter med
#laveste karakterkategori

#Kandidatens poengsum som inndata fra bruker
poengsum=int(input('Oppgi kandidatens poengsum: '))

#Tilordning av karakter ved nøsta hvis
if poengsum<40:
    karakter='F'
else:
    if poengsum<46:
        karakter='E'
    else:
        if poengsum<58:
            karakter='D'
        else:
            if poengsum<77:
                karakter='C'
            else:
                if poengsum<92:
                    karakter='B'
                else:
                    karakter='A'

#Skriv ut resultatet
print ('Ved poengsum', poengsum,'får kandidaten karakteren',karakter)
