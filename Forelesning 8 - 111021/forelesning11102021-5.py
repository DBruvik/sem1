#Program for å lese navn for navn og skrive ut de navnene som passer med
#"søkerkriteriet". Generell fremgangsmåte jfr figur 6-17 og program 6-9

#åpner fila stundent.txt
studentfil=open('student.txt','r')

#leser første linje i fila ved bruk av readline-metoden
student=studentfil.readline()

#I Python, readline returnerer en tom streng('') når den leser endoffile-merket,
#da tester vi på det.

while student!='':
    if student[0]=='O':
        print(student)
    #leser neste linje i fila
    student=studentfil.readline()


#stenger fila
studentfil.close()


#Prøv selv: ta bort linjeskift/rstrip

#print(student.rstrip('\n'))
