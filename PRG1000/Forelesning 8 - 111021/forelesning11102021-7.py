#Program for innføring av funksjoner/prosedyrer/delprogrammer

def drommebolig():
    #Her kommer kode for kalkulator 1.
    print('Du har valgt kalkulator 1, Drømmebolig.')
    print()

def lanebevis():
    #Her kommer kode for kalkulator 2.
    print('Du har valgt kalkulator 2, lånebevis.')
    print()

def main():
    fortsette=True

    while fortsette==True:
        valgtKalkulator=int(input('Hvilken kalkulator vil du bruke? '))
        if valgtKalkulator==1:
            drommebolig()
        else:
            lanebevis()

        svar=input('Ønsker du å bruke en av kalkulatorene på nytt? ')
        if svar=='nei':
            fortsette=False

#Her kommer koden for programmet/kjører main()
main()
