En=float(input('Skriv inn første tallet du tenker på: '))
To=float(input('Skriv inn andre tallet du tenker på: '))
Tre=float(input('Skriv inn tredje tallet du tenker på: '))
Fire=float(input('Skriv inn fjerde tallet du tenker på: '))
Fem=float(input('Skriv inn femte tallet du tenker på: '))

if En<To and En<Tre and En<Fire and En<Fem:
    lavesteTall=En
if To<En and To<Tre and To<Fire and To<Fem:
    lavesteTall=To
if Tre<En and Tre<To and Tre<Fire and Tre<Fem:
    lavesteTall=Tre
if Fire<En and Fire<To and Fire<Tre and Fire<Fem:
    lavesteTall=Fire
if Fem<En and Fem<To and Fem<Tre and Fem<Fire:
    lavesteTall=Fem


print('Laveste tallet i rekka du skrev inn er: ', lavesteTall)
