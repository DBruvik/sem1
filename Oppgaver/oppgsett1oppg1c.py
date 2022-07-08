baneLeie=2500
perPerson1=420
perPerson2=380
perPerson3=350
deltagere=int(input('Hvor mange deltakere er dere? '))
if deltagere>=20:
    summen=baneLeie+deltagere*perPerson3
else:
    if deltagere>=10:
        summen=baneLeie+deltagere*perPerson2
    else:
        summen=baneLeie+deltagere*perPerson1
        

    
    


print ('Det koster 2500 kr for baneleie.')
print ('Dere er',deltagere,' deltagere. Summen blir da ', summen, ' kroner.')

       
