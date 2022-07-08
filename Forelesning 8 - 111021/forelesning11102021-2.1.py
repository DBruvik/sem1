#program for å skrive 3 navn til en ny fil.

#Definer og åpner fila student.txt
studentfil=open('student.txt','w')

#Skriver 3 navn til fila
#Hver tekststreng slutter med \n

studentfil.write('Torvald\n')
studentfil.write('Kari\n')
studentfil.write('Jens\n')

#Stenge fila
studentfil.close()
