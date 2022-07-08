print('Linje Start')
minste=int(input('Skriv inn ett tall: '))
nummer=1
for n in range(2,6,1):
    print(f'Linje {n}')
    tall=int(input('Skriv inn ett tall: '))

    if tall<minste:
        minste=tall
        nummer=n

print('Ditt minste tall er',minste,'og dette er på linje',nummer)
