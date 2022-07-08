#Matematiske operatorer og operatorpresedens
#Vi bruker oppgavene i chekpoin 2.19

a=6+3*5
print ('Svaret i a)er',a)

b=12/2-4
print('Svaret i b) er',b)

c=9+14*2-6
print('Svaret i c) er',c)

d=(6+2)*3
print('Svaret i d) er',d)

e=14/(11-4)
print('Svaret i e) er',e)

f=9+12*(8-3)
print('Svaret i f)er',f)

#Formatering av desimaltall
prisPrkg=10.37
antallKg=9.6
totalpris=antallKg*prisPrkg
print('Totalprisen er: ', totalpris)

dobbelTotal=2*totalpris
print('Dobbel av totalpris er:', dobbelTotal)

#Utskrift av totalpris avrundet til 2 desimaler
print('Totalpris er:',format(totalpris, '.2f'))
