baneLeie=2500
perPerson1=420
perPerson2=380
perPerson3=350
perPerson4=400
perPerson5=450
baneLeie1=3500
baneLeie2=2000
baneLeie3=1000
deltagere=int(input('Hvor mange deltakere er dere? '))
if deltagere>=20:
    summen=baneLeie+deltagere*perPerson3
else:
    if deltagere>=10:
        summen=baneLeie+deltagere*perPerson2
    else:
        summen=baneLeie+deltagere*perPerson1
        
print ('Det koster 2500 kr for baneleie.')
print ('Dere er',deltagere,' deltagere. Summen med gammel strategi blir da ',summen, ' kroner.')

       
if deltagere<=20 and deltagere>=30:
    summen=baneLeie3+deltagere*perPerson5
else:
    if deltagere<=10:
        summen=baneLeie2+deltagere*perPerson4
    else:
        if deltagere>=9:
            summen=baneLeie1+deltagere*perPerson3
        else:
            summen=baneLeie+deltagere*perPerson1


print ('Etter ny strategi vil summen bli', summen, ' når du har', deltagere, ' deltagere med.')

        
#Skal det ligge en feilsafe med på max 30?
#Skal det komme en tydligere forkalring på beste strategien?
