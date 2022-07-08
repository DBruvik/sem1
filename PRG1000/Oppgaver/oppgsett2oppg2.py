print('Linje Start')
minste=int(input('Skriv dine tall: '))
linjeNr=1
for n in range(2,6,1):
    print(f'Linje {n}')
    nummer=int(input('Skriv dine tall: '))
    
    if nummer<minste:
        minste=nummer
        linjeNr=n
print('Ditt minste tall er:',minste,'Og dette er linje',linjeNr)
