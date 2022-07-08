#To variable for å holde orden på minste tall og tallnr, begge settes lik 0
minst=0
tallnr=0

#Fem vilkårlige tall som inndata
t1=int(input('Oppgi tall 1: '))
t2=int(input('Oppgi tall 2: '))
t3=int(input('Oppgi tall 3: '))
t4=int(input('Oppgi tall 4: '))
t5=int(input('Oppgi tall 5: '))


#Så tester vi for å finne minste tall og tallnr
if t1>t2:
    minst=t2
    tallnr=2
else:
    minst=t1
    tallnr=1

if minst>t3:
    minst=t3
    tallnr=3

if minst>t4:
    minst=t4
    tallnr=4

if minst>t5:
    minst=t5
    tallnr=5


#Så skriver vi ut resultatet, minste tall og tallnr
print('Det minste tallet er', minst,'og det tall nr',tallnr,' i rekka')

#Tegn programkart
