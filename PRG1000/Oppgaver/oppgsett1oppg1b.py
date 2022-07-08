baneLeie=2500
perPerson1=420
perPerson2=380
deltagere=int(input('Hvor mange deltakere er dere? '))
if deltagere>=10:
    summen=baneLeie+deltagere*perPerson2
else:
    summen=baneLeie+deltagere*perPerson1
    
    


print ('Det koster 2500 kr for baneleie og 420 kr per deltager.')
print ('Dere er',deltagere,' deltagere. Summen blir da ', summen, ' kroner.')

       
