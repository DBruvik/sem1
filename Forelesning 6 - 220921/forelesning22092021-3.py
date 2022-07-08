#Program som simulerer test av diskusjonenen/ELLER mellom 2 logiske utsagn

print('Vi ønsker å vurdere A>3 ELLER B<6 for ulike verdier av A og B, jfr forelesning 4 onsdag 8.9.21')

#I dette eksempelet bryter vi med at variabelnavn bør skrives med små bokstaver

#Verdien for A styres av en for løkke f.o.m 2 t.o.m verdien 5
for A in range(2,6,1):
    #Verdien på B styres av en for-løkke f.o.m 4 t.o.m 7
    for B in range(4,8,1):
        #Så lager vi en test på disjunksjonen
        if A>3 or B<6:
            print('Verdien på A er',A,'og verdien på B er',B,'disjunksjonen/ELLER er sann')
        else:
            print('Verdien på A er',A,'og verdien på B er',B,'disjunksjonen/ELLER er usann')
    print('Da er det slutt på løkka for å øke B med 1')
    print()
    print('Da øker verdien med A med 1')
print('Da er det slutt på løkka for å øke A med 1, og dermed slutt på programmet')
