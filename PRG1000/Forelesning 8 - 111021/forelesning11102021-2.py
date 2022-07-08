#Deler av oppgave 2 oppgavesett 3
#Uten kommentarer ifra lærer. Sett deg inn i oppgaven.

student=[]
print('Studenter til nå:',student)  #Kontroll print
print()

nyStudent=True  #Slepper og spørre om første er sann eller usann

while nyStudent==True:
    studnr=int(input('Oppgi studentnummer: '))
    student+=[studnr]
    fnavn=input('Oppgi fornavn: ')
    student+=[fnavn]
    studie=input('Oppgi studium: ')
    student+=[studie]
    print('Studenter til nå',student)
    print()

    svar=input('Skal det leses inn flere studenter?')
    if svar=='nei':
        nyStudent=False

listelengdeStudent=len(student)
print()
print('Lista med studenter er',student,'og består av',int(listelengdeStudent/3),'registrerte studenter')
print()

#Søke etter student på studentnr
studnr=int(input('Oppgi stundentnr på student det skal søkes på: '))
funnet=False

for indeks in range(0,listelengdeStudent,3):
    if studnr==student[indeks]:
        funnet=True
        studenten=indeks
#indeks +1 og indeks +2 er for navn og studie dersom det e rønskelig
if funnet==True:
    print('Fullstendig informasjon om studenten er: ')
    print('Studentnr: ', student[studenten])
    print('Fornavn: ',student[studenten+1])
    print('Studium: ',student[studenten+2])
else:
    print('Ingen studenter med oppgitt studentnr er registrert.')


#Prøv selv:
#1) Flytte pring inn i for-løkka, alt: løse med while
#2) Søke etter studenter på studie program
    
    


